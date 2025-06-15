from flask import Blueprint, request, jsonify
from server.models import RestaurantPizza, db, Pizza, Restaurant

restaurant_pizzas_bp = Blueprint("restaurant_pizzas", __name__, url_prefix="/restaurant_pizzas")

@restaurant_pizzas_bp.route("/", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = int(data.get("price", 0))
        pizza_id = int(data["pizza_id"])
        restaurant_id = int(data["restaurant_id"])
    except (KeyError, ValueError, TypeError):
        return jsonify({"errors": ["Invalid input"]}), 400

    if price < 1 or price > 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    new_entry = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(new_entry)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    return jsonify({
        "id": new_entry.id,
        "price": new_entry.price,
        "pizza_id": new_entry.pizza_id,
        "restaurant_id": new_entry.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }), 201
