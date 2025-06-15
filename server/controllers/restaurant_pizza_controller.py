from flask import Blueprint, request, jsonify
from server.models import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

# Define the blueprint
restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['POST'])

def create_restaurant_pizza():
    try:
        data = request.get_json()

        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        errors = []

        # Validate price range
        if price is None or not isinstance(price, int) or not (1 <= price <= 30):
            errors.append("Price must be between 1 and 30")

        # Validate existence of Pizza and Restaurant
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza:
            errors.append("Pizza not found")
        if not restaurant:
            errors.append("Restaurant not found")

        # If there are any validation errors, return them
        if errors:
            return jsonify({"errors": errors}), 400

        # Create the new restaurant-pizza association
        new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_rp)
        db.session.commit()

        # Return a joined response with pizza and restaurant details
        return jsonify({
            "id": new_rp.id,
            "price": new_rp.price,
            "pizza_id": pizza.id,
            "restaurant_id": restaurant.id,
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

    except Exception as e:
        # Show actual error to help with debugging
        return jsonify({"errors": [str(e)]}), 500
