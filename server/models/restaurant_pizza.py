from server.models import db
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    pizza_id = Column(Integer, ForeignKey('pizzas.id'), nullable=False)

    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )
