from lib.database_connection import get_flask_database_connection
from lib.book_repository import BookRepository
from lib.book import Book
from flask import request

def apply_example_routes3(app):
 ### #### ### EXERCISE
    # POST /s
    # Returns a 
    #    ; curl -
    @app.route('/count_vowels', methods=['POST'])
    def post_co_vow4():
        text = (request.form['text'])
        counter = 0
        _vowels = ['a','e','i','o','u']
        for i in text:
            if i in _vowels:
                counter += 1
        return f"The number is {counter}"

### ##### challange
    @app.route('/sort-names', methods=['POST'])
    def post_sort_names():
        data = request.form['names'].split(',')
        data = sorted(data)
        return ','.join(data)

