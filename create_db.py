"""
Run this file ONCE to create database tables
"""
from app.app import create_app
from app.extensions.db import db
from app.models.book import Book
from app.models.user import User
from app.models.review import Review


app = create_app()

with app.app_context():
    db.create_all()

    # -------------------------
    # Seed users (Admin & User)
    # -------------------------
    admin_exists = User.query.filter_by(username="admin").first()
    user_exists = User.query.filter_by(username="user").first()

    if not admin_exists:
        admin = User(
            username="admin",
            role="admin"
        )
        admin.set_password('admin123')
        db.session.add(admin)

    if not user_exists:
        user = User(
            username="user",
            role="user"
        )
        user.set_password(raw_password='user123')
        db.session.add(user)

    db.session.commit()

    print("Database tables created and users seeded successfully")
