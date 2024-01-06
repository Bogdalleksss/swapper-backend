from flask import request, jsonify
from app.models.address import Address, AddressSchema
from app.extensions import db
import uuid

addresses_schema = AddressSchema(many=True)


def delete_address(user_id, id):
    address = Address.query.get_or_404(id)

    db.session.delete(address)
    db.session.commit()

    addresses = Address.query.filter(Address.user_id == user_id)

    return jsonify({
        "status": "success",
        "data": addresses_schema.dump(addresses)
    })
