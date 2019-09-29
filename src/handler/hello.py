from flask import Blueprint, request

bp = Blueprint('hello', __name__)


@bp.route('/')
def index():
    return 'Hello, World!'

@bp.route('/echo')
def echo():
    return request.query_string
