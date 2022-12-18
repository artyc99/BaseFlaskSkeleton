from typing import Tuple, Dict

from flask import Response

CHARSET = 'utf-8'
DEFAULT_MIMETYPE = 'application/json'


def response200(data=None, charset: str = CHARSET, mimetype: str = DEFAULT_MIMETYPE) -> Response:
    if data is None:
        data = {}

    default_status = 200

    return Response(headers={'Access-Control-Allow-Origin': '*'}, response=data, mimetype=mimetype)#data, default_status, {'Content-Type': f'{mimetype}'}
