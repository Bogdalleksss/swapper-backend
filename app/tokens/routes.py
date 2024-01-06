from app.tokens import bp
import app.tokens.controller as controller
from flask_jwt_extended import jwt_required, get_jwt_identity


@bp.route('')
@jwt_required()
def get_token():
    return controller.get_tokens(get_jwt_identity())


@bp.route('', methods=['POST'])
@jwt_required()
def add_token():
    return controller.add_token(get_jwt_identity())


@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_token(id):
    return controller.delete_token(get_jwt_identity(), id)
