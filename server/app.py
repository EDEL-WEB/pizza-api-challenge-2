from flask import Flask
from .config import Config
from .models import db
from flask_migrate import Migrate


from .models.pizza import Pizza
from .models.restaurant import Restaurant
from .models.restaurant_pizza import RestaurantPizza

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    return app
