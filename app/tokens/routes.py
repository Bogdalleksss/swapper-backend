from app.tokens import bp
import app.tokens.controller as controller
from flask_jwt_extended import jwt_required, get_jwt_identity


@bp.route('', methods=['POST'])
@jwt_required()
def add_token():
    user_id = get_jwt_identity()
    return controller.add_token(user_id)


@bp.route('')
@jwt_required()
def get_token():
    user_id = get_jwt_identity()
    return controller.get_tokens(user_id)
