from lib.database_connection import get_flask_database_connection
from lib.book_repository import BookRepository
from lib.book import Book
from flask import request

def apply_example_routes2(app):
    # GET /greet
    # Returns 'Hello'
    #    ; curl http://localhost:5001/greet
    @app.route('/greet', methods=['GET'])
    def get_greet():
        name = (request.args['name'])
        return f"Hello {name}\n"
    
    # POST /greet
    # Returns 'Hello'
    #    ; curl http://localhost:5001/greet
    @app.route('/greet', methods=['POST'])
    def post_greet():
        #name = (request.args['name'])
        print(request.form['name'])
        return f"Hello\n"
    
    # GET /greet/<id>
    # Returns 'Hello, 1'
    #    ; curl http://localhost:5001/greet/1
    @app.route('/greet/<int:id>', methods=['GET'])
    def get_greets(id):
        return f"Hello {id}"



 ### #### ### EXERCISE
    # POST /submit
    # Returns a string
    #    ; curl -X POST -d "name=Pippo&message=Hello and you" http://localhost:5001/submit
    @app.route('/submit', methods=['POST'])
    def post_submit():
        a = request.form['name']
        b = request.form['message']
        return f"Thanks {a}, your sent this message: \"{b}\""

### ##### challange
    # GET /wave
    # Returns a string
    #    ; curl GET "http://localhost:5001/wave?name=Leor"
    @app.route('/wave', methods=['GET'])
    def get_wave():
        return f"I am waving at {request.args['name']}"

