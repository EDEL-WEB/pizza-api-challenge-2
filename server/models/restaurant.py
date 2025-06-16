from server.extensions import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    restaurant_pizzas = relationship('RestaurantPizza', back_populates='restaurant', cascade="all, delete")
    pizzas = association_proxy('restaurant_pizzas', 'pizza')

    def to_dict(self, include_pizzas=False):
        data = {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }

        if include_pizzas:
            data["pizzas"] = [pizza.to_dict() for pizza in self.pizzas]

        return data
