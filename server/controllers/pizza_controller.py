from flask import Blueprint, jsonify
from server.models import Pizza

pizzas_bp = Blueprint("pizzas", __name__, url_prefix="/pizzas")

@pizzas_bp.route("/", methods=["GET"])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "ingredients": p.ingredients
    } for p in pizzas]), 200
