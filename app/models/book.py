from app.extensions.db import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(200))
    summary = db.Column(db.Text)

    reviews = db.relationship("Review", backref="book", lazy=True)


"""
    book.reviews → all reviews for a book

review.book → the book for that review

--This avoids writing another relationship in Review.

    lazy=True

Controls when reviews are loaded from the database.

lazy=True is same as lazy="select":
"""