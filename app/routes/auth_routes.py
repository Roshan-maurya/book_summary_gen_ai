from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.extensions.db import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()
    # print(data.get("password"),user,'user=======')
    if not user or not user.check_password(data.get("password")):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id),additional_claims={'role':user.role})
    # token = create_access_token(identity={"id": str(user.id), "role": user.role})
    return jsonify(access_token=token)
