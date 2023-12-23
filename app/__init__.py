import eel
from flask import Flask, request, jsonify
from flask_cors import CORS
from config_app import Config
from app.swap import bp as swap_bp
from app.user import bp as user_bp
from app.transactions import bp as transaction_bp
from app.addresses import bp as addresse_bp
from app.extensions import db, ma, jwt
import multiprocessing

from app.models.user import User, UserSchema


def start_eel():
    eel.init('app/dist/spa')
    eel.start('index.html', mode='chrome', port=5030)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    eel_process = multiprocessing.Process(target=start_eel, args=())
    eel_process.start()

    # Extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    # Modules
    app.register_blueprint(swap_bp)
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(transaction_bp, url_prefix="/transactions")
    app.register_blueprint(addresse_bp, url_prefix="/addresses")

    @app.route('/auth', methods=['POST'])
    def auth():
        user_auth = User.authenticate(request.json['access_key'])
        token = user_auth.get_token()
        return jsonify({
            "status": "success",
            "access_token": token
        })

    return app
