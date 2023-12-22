from app.user import bp
import app.user.controller as controller
from flask_jwt_extended import jwt_required, get_jwt_identity


@bp.route('/create', methods=['POST'])
@jwt_required()
def create_user():
    return controller.create_user()


@bp.route('/all')
@jwt_required()
def get_users():
    return controller.get_users()


@bp.route('/me')
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    return controller.get_user(user_id)


@bp.route('/edit/me', methods=['POST'])
@jwt_required()
def edit_me():
    user_id = get_jwt_identity()
    return controller.edit_me(user_id)
