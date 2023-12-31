from datetime import datetime, timedelta
from app.extensions import db, ma


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    chain = db.Column(db.Integer)
    hash = db.Column(db.String(300))
    icon = db.Column(db.String(300))
    token_from = db.Column(db.String(300))
    token_from_quantity = db.Column(db.Float)
    token_to = db.Column(db.String(300))
    token_to_quantity = db.Column(db.Float)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Transaction %r>' % self.id


class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction
        sql_session = db.session
