from server.models import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.associationproxy import association_proxy

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)

    # Relationship to the join table
    restaurant_pizzas = relationship(
        'RestaurantPizza',
        backref='pizza',
        cascade='all, delete-orphan'
    )

    # Indirect relationship to Restaurant via RestaurantPizza
    restaurants = association_proxy('restaurant_pizzas', 'restaurant')
