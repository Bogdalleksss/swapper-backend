from datetime import datetime, timedelta
from app.extensions import db, ma


class Tokens(db.Model):
    __tablename__ = 'tokens'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    chain = db.Column(db.Integer)
    address = db.Column(db.String(300))
    token = db.Column(db.String(300))
    balance = db.Column(db.Float)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Tokens %r>' % self.id


class TokensSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tokens
        sql_session = db.session
