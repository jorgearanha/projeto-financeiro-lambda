from src.https import HttpResponse
import json


class HttpBaseException(Exception):
    def __init__(self, ret: HttpResponse, body=None):
        self.dict_return = ret
        self.body = body

    def get_response(self):
        if isinstance(self.body, dict):
            self.body = json.dumps(self.body)

        self.dict_return['body'] = self.body
        return self.dict_return


class NotFoundException(HttpBaseException):
    def __init__(self, body=None):
        super().__init__(HttpResponse.not_found(), body)


class BadRequestException(HttpBaseException):
    def __init__(self, body=None):
        super().__init__(HttpResponse.bad_request(), body)


class UnauthorizedException(HttpBaseException):
    def __init__(self, body=None):
        super().__init__(HttpResponse.unauthorized(), body)


class ForbiddenException(HttpBaseException):
    def __init__(self, body=None):
        super().__init__(HttpResponse.forbidden(), body)


class UnprocessableException(HttpBaseException):
    def __init__(self, body=None):
        super().__init__(HttpResponse.unprocessable(), body)


class ErrorException(HttpBaseException):
    def __init__(self, body=None):
        super().__init__(HttpResponse.error(), body)


class CustomException(HttpBaseException):
    def __init__(self, status_code, body=None):
        super.__init__(HttpResponse.build(status_code), body)


class JaCorrentistaException(UnauthorizedException):
    pass


class AtacadoException(UnauthorizedException):
    pass


class FiltroPLDException(UnauthorizedException):
    pass


class PortePException(UnauthorizedException):
    pass


class PortePVermelhoException(UnauthorizedException):
    pass