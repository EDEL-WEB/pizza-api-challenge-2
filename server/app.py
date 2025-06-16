from flask import Flask, jsonify
from server.config import Config
from server.extensions import db, migrate
from server.controllers import all_controllers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from server import models  # 👈 ADD THIS LINE AFTER db.init_app()

    for controller in all_controllers:
        app.register_blueprint(controller)

    @app.route("/")
    def index():
        return jsonify({"message": "🍕 Pizza API is running!"}), 200

    return app
