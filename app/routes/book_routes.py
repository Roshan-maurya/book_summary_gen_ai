from flask import Blueprint, request, jsonify,current_app
from flask_jwt_extended import jwt_required
from app.models.book import Book
from app.models.review import Review
from app.extensions.db import db
from app.services.ai_service import generate_summary
from app.utils.role_required import role_required


#  to generate summary when you save data in books table
from threading import Thread
from app.services.background_summary import generate_summary_background

book_bp = Blueprint("books", __name__)

@book_bp.route("/books", methods=["POST"])
@jwt_required()
@role_required("admin")
def add_book():
    data = request.json
    # Step 1: Save book with placeholder summary
    book = Book(
        title=data.get("title"),
        author=data.get("author"),
        summary="Generating summary..."
    )
    db.session.add(book)
    db.session.commit()  # book.id is now available

    # Step 2: Run background thread to generate summary
    # Pass the real Flask app into the thread
    Thread(
        target=generate_summary_background,
        args=(current_app._get_current_object(), book.id, data.get("content"))
    ).start()

    # Step 3: Return immediate response
    return jsonify({
        "message": "Book added successfully",
        "book_id": book.id,
        "summary_status": "Processing"
    }), 202
    # summary = generate_summary(data.get("content"))
    # print(summary)
    # # summary = ''
    # book = Book(
    #     title=data.get("title"),
    #     author=data.get("author"),
    #     summary=summary
    # )
    # db.session.add(book)
    # db.session.commit()

    # return jsonify({"message": "Book added", "summary": summary})

@book_bp.route("/books", methods=["GET"])
@jwt_required()
def get_books():
    books = Book.query.all()
    return jsonify([{"id": b.id, "title": b.title, "author": b.author} for b in books])


@book_bp.route("/books/<int:id>", methods=["GET"])
@jwt_required()
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "summary": book.summary
    })


@book_bp.route("/books/<int:id>", methods=["PUT"])
@jwt_required()
@role_required("admin")
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.json

    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)

    db.session.commit()
    return jsonify({"message": "Book updated"})


@book_bp.route("/books/<int:id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})

@book_bp.route("/books/<int:id>/reviews", methods=["POST"])
@jwt_required()
@role_required("user")
def add_review(id):
    data = request.json
    review = Review(
        rating=data.get("rating"),
        comment=data.get("comment"),
        book_id=id
    )
    db.session.add(review)
    db.session.commit()
    return jsonify({"message": "Review added"}), 201

@book_bp.route("/books/<int:id>/reviews", methods=["GET"])
@jwt_required()
def get_reviews(id):
    reviews = Review.query.filter_by(book_id=id).all()
    return jsonify([
        {"rating": r.rating, "comment": r.comment}
        for r in reviews
    ])



@book_bp.route("/books/<int:id>/summary", methods=["GET"])
@jwt_required()
def book_summary(id):
    book = Book.query.get_or_404(id)
    reviews = Review.query.filter_by(book_id=id).all()

    avg_rating = (
        sum(r.rating for r in reviews) / len(reviews)
        if reviews else None
    )

    return jsonify({
        "title": book.title,
        "summary": book.summary,
        "average_rating": avg_rating
    })


@book_bp.route("/recommendations", methods=["GET"])
@jwt_required()
@role_required("user")
def recommendations():
    books = Book.query.limit(5).all()
    return jsonify([
        {"id": b.id, "title": b.title, "author": b.author}
        for b in books
    ])



@book_bp.route("/generate-summary", methods=["POST"])
@jwt_required()
def ai_summary():
    data = request.json
    summary = generate_summary(data.get("content"))
    return jsonify({"summary": summary})

