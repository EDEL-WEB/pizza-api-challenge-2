from flask import Flask, jsonify
from server.config import Config
from server.extensions import db, migrate  # db and migrate from extensions
from server.controllers import all_controllers  # list of registered blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register all blueprints (e.g. /pizzas, /restaurants, etc.)
    for controller in all_controllers:
        app.register_blueprint(controller)

    # Root route for testing
    @app.route("/")
    def index():
        return jsonify({"message": "🍕 Pizza API is running!"}), 200

    return app
