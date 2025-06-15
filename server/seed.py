from server.app import create_app
from server.models import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    print(" Seeding database...")

    
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    
    pizza1 = Pizza(name="Margherita", ingredients="cheese, tomato sauce, basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="cheese, tomato sauce, pepperoni")
    pizza3 = Pizza(name="Hawaiian", ingredients="cheese, ham, pineapple")

    db.session.add_all([pizza1, pizza2, pizza3])
    db.session.commit()

    
    rest1 = Restaurant(name="Mama's Pizza", address="123 Main St, Homa Bay")
    rest2 = Restaurant(name="Pizza Palace", address="456 Market Rd, Nairobi")

    db.session.add_all([rest1, rest2])
    db.session.commit()

    
    rp1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=rest1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=pizza2.id, restaurant_id=rest1.id)
    rp3 = RestaurantPizza(price=15, pizza_id=pizza3.id, restaurant_id=rest2.id)
    rp4 = RestaurantPizza(price=11, pizza_id=pizza1.id, restaurant_id=rest2.id)

    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

    print(" Done seeding!")
