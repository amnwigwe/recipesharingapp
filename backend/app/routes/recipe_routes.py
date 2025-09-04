from flask import Blueprint, request, jsonify
from db import init_db

conn = init_db()
bp = Blueprint("recipes", __name__, url_prefix="/recipes")

@bp.route("", methods=["GET"])
def get_recipes():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    cursor.close()
    return jsonify(recipes)

@bp.route("", methods=["POST"])
def add_recipe():
    data = request.json
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO recipes (title, ingredients, instructions) VALUES (%s,%s,%s)",
        (data["title"], data["ingredients"], data["instructions"])
    )
    conn.commit()
    data["id"] = cursor.lastrowid
    cursor.close()
    return jsonify(data), 201
