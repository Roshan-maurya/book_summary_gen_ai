# from flask import current_app
from app.models.book import Book
from app.extensions.db import db
from app.services.ai_service import generate_summary

def generate_summary_background(app, book_id, content):
    """
    Background function to generate book summary and update the database.
    This function runs in a separate thread.
    """
    # Explicitly push Flask app context
    with app.app_context():
        try:
            summary = generate_summary(content)

            book = Book.query.get(book_id)
            if book:
                book.summary = summary
                db.session.commit()

        except Exception as e:
            db.session.rollback()
            print(f"Error generating summary for book {book_id}: {e}")
