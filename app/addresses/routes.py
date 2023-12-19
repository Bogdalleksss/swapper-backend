from app.transactions import bp
import app.transactions.controller as controller
from flask_jwt_extended import jwt_required, get_jwt_identity


# @bp.route('/create', methods=['POST'])
# @jwt_required()
# def create_user():
#     return controller.create_transaction()
#
#
# @bp.route('/all')
# @jwt_required()
# def get_users():
#     return controller.get_transactions()
