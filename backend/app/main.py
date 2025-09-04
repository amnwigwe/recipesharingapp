from flask import Flask
from flask_cors import CORS
from db import init_db
from routes.auth_routes import bp as auth_bp
from routes.recipe_routes import bp as recipe_bp

app = Flask(__name__)
CORS(app)

init_db()  # <- initialize MySQL connection

app.register_blueprint(auth_bp)
app.register_blueprint(recipe_bp)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
