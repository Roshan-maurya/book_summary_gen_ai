from app.extensions.db import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(255))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
