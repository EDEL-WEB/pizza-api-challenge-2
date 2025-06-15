from server.models import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.associationproxy import association_proxy

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    restaurant_pizzas = relationship(
        'RestaurantPizza',
        backref='restaurant',
        cascade='all, delete-orphan'
    )

    pizzas = association_proxy('restaurant_pizzas', 'pizza')
