from app.addresses import bp
import app.addresses.controller as controller
from flask_jwt_extended import jwt_required, get_jwt_identity


@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_address(id):
    return controller.delete_address(get_jwt_identity(), id)

