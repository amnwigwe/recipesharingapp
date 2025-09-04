from flask import Blueprint, request, jsonify
from db import init_db

conn = init_db()  # initialize here

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (%s,%s,%s)",
        (data["username"], data["email"], data["password"])
    )
    conn.commit()
    cursor.close()
    return jsonify({"message": "User registered"})

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (data["email"], data["password"])
    )
    user = cursor.fetchone()
    cursor.close()
    if user:
        return jsonify({"message": "Login successful", "user": {"id": user["id"], "username": user["username"], "email": user["email"]}})
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    
# NEW PROFILE ROUTE
@bp.route("/profile/<int:user_id>", methods=["GET"])
def profile(user_id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, username, email FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return jsonify({"user": user})
    else:
        return jsonify({"message": "User not found"}), 404
