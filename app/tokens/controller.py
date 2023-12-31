from flask import request, jsonify
from app.extensions import db
from app.models.tokens import Tokens, TokensSchema
from sqlalchemy import and_, or_

tokens_schema = TokensSchema(many=True)


def add_token(user_id):
    token_data = request.json
    is_token = db.session.query(Tokens.query.filter(Tokens.address == token_data['address']).exists()).scalar()

    print(is_token)

    if not is_token:
        token = Tokens(
            **token_data,
            user_id=user_id,
        )
        db.session.add(token)
        db.session.commit()

    tokens = Tokens.query.all()

    return jsonify({
        "status": "success",
        "data": tokens_schema.dump(tokens)
    })


def get_tokens(user_id):
    tokens = Tokens.query.filter(Tokens.user_id == user_id)

    return {
        "status": "success",
        "data": tokens_schema.dump(tokens)
    }