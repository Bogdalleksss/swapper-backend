from datetime import datetime
from app.extensions import db, ma


class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    wallet_address = db.Column(db.String(300))
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Address %r>' % self.id


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        sql_session = db.session
