from flask import Blueprint, request, jsonify
from ..models.recipe_model import create_recipe, get_all_recipes
from ..routes.auth_routes import SECRET_KEY
import jwt
from functools import wraps

bp = Blueprint('recipes', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message':'Token missing'}),401
        try:
            data = jwt.decode(token.split()[1], SECRET_KEY, algorithms=['HS256'])
            request.user_id = data['user_id']
        except:
            return jsonify({'message':'Invalid token'}),401
        return f(*args, **kwargs)
    return decorated

@bp.get("/api/v1/recipes")
def list_recipes():
    search = request.args.get('search')
    tag = request.args.get('tag')
    recipes = get_all_recipes(search, tag)
    return jsonify(recipes)

@bp.post("/api/v1/recipes")
@token_required
def add_recipe():
    data = request.get_json()
    recipe = create_recipe(data['title'], data['ingredients'], data['instructions'], data.get('image_url'), data.get('tags'), request.user_id)
    return jsonify(recipe),201