import requests
from flask import request
from uniswap import Uniswap
from web3 import Web3
from web3.middleware import geth_poa_middleware
from app.models.user import User, UserSchema
from app.models.address import Address, AddressSchema
from app.models.transaction import Transaction, TransactionSchema
from app.extensions import db

inch_base_url = 'https://api.1inch.dev'

user_schema = UserSchema()


def get_uniswap(provider, user_id):
    private_key = request.headers.get('private_key')
    user = User.query.filter(User.id == user_id).one()

    print(user.wallet_address)

    return Uniswap(address=user.wallet_address, private_key=private_key, provider=provider, version=3)


def get_web3(provider):
    w3 = Web3(Web3.HTTPProvider(provider))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return w3


def get_eth_balance():
    provider = request.args.get('rpc')
    address = request.args.get('address')

    w3 = get_web3(provider)
    balance = w3.eth.get_balance(account=w3.to_checksum_address(address))

    return {
        'balance': balance
    }


def get_approve_spender(user_id):
    user = User.query.filter(User.id == user_id).one()

    chain = request.args.get('chain')
    url = inch_base_url + f'/swap/v5.2/{chain}/approve/spender'

    print(user.inch_api_swap_key)

    return requests.get(url=url, headers={'Authorization': f'Bearer {user.inch_api_swap_key}'}).json()


def get_allowance(user_id):
    user = User.query.filter(User.id == user_id).one()
    chain = request.args.get('chain')
    token = request.args.get('token')
    address = user.wallet_address

    url = inch_base_url + f'/swap/v5.2/{chain}/approve/allowance?tokenAddress={token}&walletAddress={address}'
    return requests.get(url=url, headers={'Authorization': f'Bearer {user.inch_api_swap_key}'}).json()


def get_quote(user_id):
    user = User.query.filter(User.id == user_id).one()

    chain = request.args.get('chain')
    token_to = request.args.get('tokenTo')
    token_from = request.args.get('tokenFrom')
    amount = request.args.get('amount')

    params = {
        'src': token_from,
        'dst': token_to,
        'amount': amount,
        'includeTokensInfo': 'true',
        'includeProtocols': 'true'
    }

    url = inch_base_url + f'/swap/v5.2/{chain}/quote'
    r = requests.get(url=url, params=params, headers={'Authorization': f'Bearer {user.inch_api_key}'})
    try:
        return r.json()
    except:
        return {}


def get_swap_data(user_id):
    user = User.query.filter(User.id == user_id).one()

    chain = request.args.get('chain')
    token_to = request.args.get('tokenTo')
    token_from = request.args.get('tokenFrom')
    amount = request.args.get('amount')
    slippage = request.args.get('slippage')
    receiver = request.args.get('receiver')

    params = {
        'src': token_from,
        'dst': token_to,
        'amount': amount,
        'includeTokensInfo': 'true',
        'includeProtocols': 'true',
        'slippage': slippage,
        'from': user.wallet_address
    }
    if receiver:
        params['receiver'] = receiver

    url = inch_base_url + f'/swap/v5.2/{chain}/swap'
    r = requests.get(url=url, params=params, headers={'Authorization': f'Bearer {user.inch_api_swap_key}'})
    try:
        return r.json()
    except:
        return {}


def get_token_info(user_id):
    provider = request.args.get('rpc')
    address = request.args.get('address')

    uniswap = get_uniswap(provider, user_id)
    w3 = get_web3(provider)

    token = uniswap.get_token(address=w3.to_checksum_address(address))
    balance = uniswap.get_token_balance(token=token.address)
    return {
        'address': token.address,
        'name': token.name,
        'symbol': token.symbol,
        'decimals': token.decimals,
        'balance': balance
    }


def get_token_balance(user_id):
    provider = request.args.get('rpc')
    address = request.args.get('address')

    uniswap = get_uniswap(provider, user_id)
    w3 = get_web3(provider)

    token = uniswap.get_token(address=w3.to_checksum_address(address))
    token_balance = uniswap.get_token_balance(token=w3.to_checksum_address(address))

    return str(token_balance / 10 ** token.decimals)


def add_address(user_id):
    address_data = request.json
    print(address_data)

    if not address_data['wallet_address'] or not address_data['name']:
        return {
            "status": "error",
        }

    address_schema = AddressSchema()
    address = Address(
        **address_data,
        user_id=user_id
    )
    db.session.add(address)
    db.session.commit()

    return {
        "status": "success",
        "data": address_schema.dump(address)
    }


def get_addresses(user_id):
    addresses = Address.query.filter(Address.user_id == user_id)
    addresses_schema = AddressSchema(many=True)

    return {
        "status": "success",
        "data": addresses_schema.dump(addresses)
    }


def add_transaction(user_id):
    transaction_data = request.json

    if not transaction_data['hash'] or not transaction_data['chain']:
        return {
            "status": "error",
        }

    transaction_schema = TransactionSchema()
    transaction = Transaction(
        **transaction_data,
        user_id=user_id
    )
    db.session.add(transaction)
    db.session.commit()

    return {
        "status": "success",
        "data": transaction_schema.dump(transaction)
    }


def get_transactions(user_id):
    transactions = Transaction.query.filter(Transaction.user_id == user_id)
    transactions_schema = TransactionSchema(many=True)

    return {
        "status": "success",
        "data": transactions_schema.dump(transactions)
    }
