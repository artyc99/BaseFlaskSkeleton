import json

from flask import Blueprint, jsonify

from backend.app.response import response200

rsaApi = Blueprint('rsaApi', __name__)


@rsaApi.route('/api/rsa/test', methods=['POST', 'GET'])
def test():
    return response200(json.dumps({'test': 'test', 'test2':'test2'}), mimetype='application/json')
