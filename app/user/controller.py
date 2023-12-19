from flask import request, jsonify
from app.models.user import User, UserSchema
from app.extensions import db
import uuid


def create_user():
    user_schema = UserSchema()
    user = User(
        access_key=str(uuid.uuid4())
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "status": "success",
        "data": user_schema.dump(user)
    })


def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)

    return jsonify({
        "status": "success",
        "data": user_schema.dump(users)
    })


def get_user(user_id):
    user = User.query.filter(User.id == user_id).one()
    user_schema = UserSchema()
    output = user_schema.dump(user)

    return jsonify({
        "status": "success",
        "data": {
            "id": output['id'],
            "inch_api_key": output['inch_api_key'],
            "inch_api_swap_key": output['inch_api_swap_key'],
            "wallet_address": output['wallet_address']
        }
    })
