from app.swap import bp
import app.swap.controller as controller
from app_config import config
from flask_jwt_extended import jwt_required, get_jwt_identity


@bp.route('/get_config')
@jwt_required()
def get_settings():
    return config


@bp.route('/get_eth_balance')
@jwt_required()
def get_balances():
    return controller.get_eth_balance()


@bp.route('/get_approve_spender')
@jwt_required()
def get_approve_spender():
    user_id = get_jwt_identity()
    return controller.get_approve_spender(user_id)


@bp.route('/get_allowance')
@jwt_required()
def get_allowance():
    user_id = get_jwt_identity()
    return controller.get_allowance(user_id = get_jwt_identity())


@bp.route('/get_qoute')
@jwt_required()
def get_quote():
    user_id = get_jwt_identity()
    return controller.get_quote(user_id)


@bp.route('/get_swap_data')
@jwt_required()
def get_swap_data():
    user_id = get_jwt_identity()
    return controller.get_swap_data(user_id)


@bp.route('/get_token_info')
@jwt_required()
def get_token_info():
    user_id = get_jwt_identity()
    return controller.get_token_info(user_id)


@bp.route('/get_token_balance')
@jwt_required()
def get_token_balance():
    user_id = get_jwt_identity()
    return controller.get_token_balance(user_id)


@bp.route('/add_address', methods=['POST'])
@jwt_required()
def add_address():
    user_id = get_jwt_identity()
    return controller.add_address(user_id)


@bp.route('/get_addresses')
@jwt_required()
def get_addresses():
    user_id = get_jwt_identity()
    return controller.get_addresses(user_id)


@bp.route('/add_transaction', methods=['POST'])
@jwt_required()
def add_transaction():
    user_id = get_jwt_identity()
    return controller.add_transaction(user_id)


@bp.route('/get_transactions')
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    return controller.get_transactions(user_id)