from flask import Blueprint, request, jsonify
import jwt
from .auth_routes import SECRET_KEY

bp_me = Blueprint('auth_me', __name__)

def token_required(f):
    from functools import wraps
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

@bp_me.get("/auth/me")
@token_required
def me():
    return jsonify({'user_id': request.user_id})