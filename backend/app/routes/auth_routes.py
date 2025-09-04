from flask import Blueprint, request, jsonify
from ..models.user_model import create_user, get_user_by_email
import bcrypt
import jwt
import os

bp = Blueprint('auth', __name__)

SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

@bp.post("/auth/register")
def register():
    data = request.get_json()
    user = create_user(data['username'], data['email'], data['password'])
    return jsonify(user), 201

@bp.post("/auth/login")
def login():
    data = request.get_json()
    user = get_user_by_email(data['email'])
    if user and bcrypt.checkpw(data['password'].encode(), user['password_hash'].encode()):
        token = jwt.encode({'user_id': user['id']}, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401