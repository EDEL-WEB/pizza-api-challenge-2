 Pizza API
A RESTful API built with Flask, SQLAlchemy, and Flask-Migrate that allows clients to:

View a list of pizzas 

View restaurants 

Associate pizzas with restaurants, including price

Delete restaurants with cascading deletes

Validate inputs and return meaningful error messages



clone this repo:https://github.com/EDEL-WEB/pizza-api-challenge-2.git



 Project Structure

pizza-api-challenge-2/
├── server/
│   ├── __init__.py
│   ├── app.py                 # App factory
│   ├── config.py              # Configuration (e.g., DB URI)
│   ├── extensions.py          # SQLAlchemy & Migrate setup
│   ├── controllers/
│   │   ├── __init__.py        # Register all controllers (Blueprints)
│   │   ├── pizza_controller.py
│   │   ├── restaurant_controller.py
│   │   └── restaurant_pizza_controller.py
│   └── models/
│       ├── __init__.py
│       ├── pizza.py
│       ├── restaurant.py
│       └── restaurant_pizza.py
├── migrations/
│   └── ...                    # Database migration scripts
├── README.md
└── requirements.txt
 Setup Instructions


 
1.  Create a virtual environment
pipenv install&&pipenv shell
2.  Install dependencies


3.  Set up the environment

export FLASK_APP=server.app:create_app
4.  Initialize the database

flask db init      # Only once
flask db migrate -m "Initial migration"
flask db upgrade
5.  Run the server

flask run --port=5000
API will be available at: http://127.0.0.1:5000

 Models
 Pizza

id: Integer, PK  
name: String, required  
ingredients: String, required  
 Restaurant
python

id: Integer, PK  
name: String, required  
address: String, required  
 RestaurantPizza (Join table)


id: Integer, PK  
price: Integer (1–30), required  
pizza_id: FK → Pizza.id  
restaurant_id: FK → Restaurant.id  
 Includes validation using CheckConstraint.

 API Endpoints
GET /pizzas
Returns all pizzas.




[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "cheese, tomato sauce, basil"
  }
]
GET /restaurants
Returns all restaurants with limited info.

GET /restaurants/<id>
Returns a specific restaurant and the pizzas it serves.

json
Copy
Edit
{
  "id": 1,
  "name": "Dominos",
  "address": "123 Main St",
  "pizzas": [
    { "id": 1, "name": "Pepperoni", "ingredients": "cheese, tomato, pepperoni" },
    ...
  ]
}
DELETE /restaurants/<id>
Deletes a restaurant and its associated RestaurantPizza records (cascading delete).

POST /restaurant_pizzas
Creates a new RestaurantPizza record (pizza offered at a restaurant).

Request:


{
  "price": 15,
  "pizza_id": 4,
  "restaurant_id": 3
}
Success Response:


{
  "id": 8,
  "price": 15,
  "pizza_id": 4,
  "restaurant_id": 3,
  "pizza": {
    "id": 4,
    "name": "Hawaiian",
    "ingredients": "cheese, ham, pineapple"
  },
  "restaurant": {
    "id": 3,
    "name": "Mama's Kitchen",
    "address": "456 Local St"
  }
}
Error Response (e.g. pizza not found):


{
  "errors": ["Pizza not found"]
}
 ##  API Testing

Use the provided Postman collection to test all API routes:

1. Open [Postman](https://www.postman.com/)
2. Click Import
3. Upload the file: `challenge-1-pizzas.postman_collection.json`
4. Make sure your Flask server is running at `http://localhost:5000`
5. Send requests to test routes like:
   - GET /restaurants
   - POST /restaurant_pizzas
   - DELETE /restaurants/<id>


Common Issues
1.  Pizza not found
Double-check the pizza_id in your database. You can view existing pizzas with:

bash
Copy
Edit
curl http://127.0.0.1:5000/pizzas/
2.  The current Flask app is not registered with this 'SQLAlchemy' instance
Make sure you are:

Using create_app pattern properly

Calling db.init_app(app) in app.py

Running the server via:

export FLASK_APP=server.app:create_app
flask run --port=5000
 Tips
Use PostgreSQL in production (easily replace SQLite).

Use Flask-Migrate to track DB changes.

Separate concerns: models, controllers, config, etc.

Use .to_dict() methods for consistent serialization.

 Author
Built with  by Edel Omondi during a backend Flask API challenge.

