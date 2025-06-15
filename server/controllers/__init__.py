from .restaurant_controller import restaurants_bp
from .pizza_controller import pizzas_bp
from .restaurant_pizza_controller import restaurant_pizzas_bp

all_controllers = [restaurants_bp, pizzas_bp, restaurant_pizzas_bp]
