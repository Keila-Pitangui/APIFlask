from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# DataBase

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db) 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

if __name__ == '__main__':
    app.run(debug=True)

# CRUD

usuarios = []

@app.route('/user', methods=['GET'])
def get_user():
    return jsonify(user)

@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.get_json()
    user.append(new_user)
    return jsoninfy(new_user), 201

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    user = next((u for u in user if u['id'] == id), None)
    if user is None:
        return jsonify({'message':'Usuário não encontrado'}), 404
    data = request.get_json()
    user.update(data)
    return jsoninfy(user)

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = next((u for u in user if u['id'] == id), None)
    if user is None:
        return jsonify({'message':'Usuário não encontrado'}), 404
    user.remove(user)
    return '', 204

# export FLASK_APP=app.py
