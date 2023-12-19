from flask import Blueprint

bp = Blueprint('swap', __name__)

from app.swap import routes
