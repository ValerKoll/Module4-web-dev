import os
from flask import Flask, request

# new flask app
app = Flask(__name__)

# ===== routing =====
@app.route('/wave', methods=['GET'])
def get_name():
    name = request.args['name']
    return f"hello I am {name}"

@app.route('/wave', methods=['POST'])
def post_name():
    name = request.form['name']
    meet = request.form['meet']
    return f"hi {name} nice to meet you, I am {meet}"

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    data = request.form['names'].split(',')
    data = sorted(data)
    return ','.join(data)

# ===== CHALLENGE GOES HERE ======
#
@app.route('/add_name', methods=['GET'])
def add_name():
    name = request.args['add']
    list_of_names = ['Julia', 'Alice', 'Karim']
    list_of_names.append(name)
    return ', '.join(list_of_names)
#
# ===== CHALLENGE end ============

# === end routing ===
#    port 5000     <========
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT',5000)))