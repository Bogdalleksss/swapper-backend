from flask import request, jsonify
from app.models.transaction import Transaction, TransactionSchema
from app.extensions import db
import uuid


# def create_transactions():
#     transaction_schema = TransactionSchema()
#     user = Transaction(
#         access_key=str(uuid.uuid4())
#     )
#     db.session.add(user)
#     db.session.commit()
#
#     return jsonify({
#         "status": "success",
#         "data": transaction_schema.dump(user)
#     })
#
#
# def get_transactions():
#     transactions = Transaction.query.all()
#     transaction_schema = TransactionSchema(many=True)
#
#     return jsonify({
#         "status": "success",
#         "data": transaction_schema.dump(transactions)
#     })
