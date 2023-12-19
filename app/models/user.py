from datetime import datetime, timedelta
from app.extensions import db, ma
from flask_jwt_extended import create_access_token


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    access_key = db.Column(db.String(300))
    wallet_address = db.Column(db.String(300))
    inch_api_key = db.Column(db.String(300))
    inch_api_swap_key = db.Column(db.String(300))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id,
            expires_delta=expire_delta
        )
        return token

    @classmethod
    def authenticate(cls, access_key):
        is_user = db.session.query(cls.query.filter(cls.access_key == access_key).exists()).scalar()

        if not is_user:
            raise Exception('User not found')

        return cls.query.filter(cls.access_key == access_key).one()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sql_session = db.session
