from flask import Blueprint, jsonify, request
from server.models import Restaurant, RestaurantPizza, db

restaurants_bp = Blueprint("restaurants", __name__, url_prefix="/restaurants")

@restaurants_bp.route("/", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "address": r.address
    } for r in restaurants]), 200

@restaurants_bp.route("/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [{
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        } for pizza in restaurant.pizzas]
    }), 200

@restaurants_bp.route("/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return "", 204
