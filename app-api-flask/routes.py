from flask import Blueprint, jsoninfy, request
from app import db
from app.models import User

main = Blueprint('main', __name__)

@main.route('/user', methods=['GET'])
def get_user():
    user = User.query.all()
    return jsoninfy([user.as_dict() for user in users])

@main.route('/user', methods=['POST'])
def create_user():
    new_user = request.get_json()
    user = User(nome=new_user['name'], email=new_user['email'])
    db.session.add(user)
    db.session.commit()
    return jsoninfy(user.as_dict()), 201
