from flask import Blueprint, request, jsonify
from ..models.favorites_model import add_favorite, remove_favorite, list_favorites
from ..routes.auth_routes import SECRET_KEY
import jwt
from functools import wraps

bp_fav = Blueprint('favorites', __name__)

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

@bp_fav.post("/api/v1/favorites/<int:recipe_id>")
@token_required
def toggle_favorite(recipe_id):
    # Check if already favorited
    existing = list_favorites(request.user_id)
    ids = [r['id'] for r in existing]
    if recipe_id in ids:
        remove_favorite(request.user_id, recipe_id)
        return jsonify({'message':'Removed from favorites'})
    else:
        add_favorite(request.user_id, recipe_id)
        return jsonify({'message':'Added to favorites'})

@bp_fav.get("/api/v1/favorites")
@token_required
def get_favorites():
    favs = list_favorites(request.user_id)
    return jsonify(favs)