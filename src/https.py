from enum import Enum
import json
from decimal import Decimal

headers = {
    'Access-Control-Allow-Headers': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': '*'
}


def _custom_response(status_code, body=None, json_encoder=None):
    if isinstance(status_code, HttpStatusCode):
        status_code = status_code.value

    if isinstance(body, dict):
        body = json.dumps(body, cls=json_encoder)

    return dict(statusCode=status_code, headers=headers, body=body)


class HttpResponse(object):

    @staticmethod
    def success(body=None, json_encoder=None):
        return _custom_response(HttpStatusCode.OK, body, json_encoder)

    @staticmethod
    def created():
        return _custom_response(HttpStatusCode.CREATED)

    @staticmethod
    def no_content():
        return _custom_response(HttpStatusCode.NO_CONTENT)

    @staticmethod
    def bad_request():
        return _custom_response(HttpStatusCode.BAD_REQUEST)

    @staticmethod
    def unauthorized():
        return _custom_response(HttpStatusCode.UNAUTHORIZED)

    @staticmethod
    def forbidden():
        return _custom_response(HttpStatusCode.FORBIDDEN)

    @staticmethod
    def not_found():
        return _custom_response(HttpStatusCode.NOT_FOUND)

    @staticmethod
    def unprocessable():
        return _custom_response(HttpStatusCode.UNPROCESSABLE)

    @staticmethod
    def error():
        return _custom_response(HttpStatusCode.ERROR)

    @staticmethod
    def build(status_code, body=None, json_encoder=None):
        return _custom_response(status_code, body, json_encoder)


class HttpStatusCode(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    UNPROCESSABLE = 422
    ERROR = 500


class HttpMethod(Enum):
    DELETE = 'DELETE'
    GET = 'GET'
    OPTIONS = 'OPTIONS'
    PATCH = 'PATCH'
    POST = 'POST'
    PUT = 'PUT'


class CustomJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(CustomJsonEncoder, self).default(obj)
