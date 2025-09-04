from flask import Flask
from flask_cors import CORS
from .db import init_db
from .routes.auth_routes import bp as auth_bp
from .routes.recipe_routes import bp as recipe_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    init_db()
    app.register_blueprint(auth_bp)
    app.register_blueprint(recipe_bp)
    from .routes.auth_me_routes import bp_me
    app.register_blueprint(bp_me)
    from .routes.favorites_routes import bp_fav
    app.register_blueprint(bp_fav)
    return app

if __name__=="__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)