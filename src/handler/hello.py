from flask import Blueprint

bp = Blueprint('hello', __name__)


@bp.route('/')
def index():
    return 'Hello, World!'

@bp.route('/echo')
def echo():
    return 'Hello, World!'
