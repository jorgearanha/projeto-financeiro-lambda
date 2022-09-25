from src.controller import *
from src.commons import config
from src.https import HttpResponse
from src.exceptions import HttpBaseException

# __logger = config.logger(__name__)

def lambda_handler(event, context):
    try:
        resource = event.get('resource', None)
        assert resource, 'Resource is required'

        method = event.get('httpMethod', None)
        assert method, 'HttpMethod is required'

        function = routes.routes.get(resource + method, None)
        assert function, 'Invalid resource path resource %s method %s' % (resource, method)

        return function(event, context)
    except AssertionError as err:
        # __logger.info(f'[lambda_handler] failure... {err.args[0]}')
        raise HttpBaseException(HttpResponse.bad_request(), err.args[0])


if __name__ == '__main__':
    event = {
        'resource': '/saidas',
        'httpMethod': 'GET',
        'pathParameters': {
            'referencia': '202009',
            'id_code': 'SAOOE202008'
        },
        'body':{
            "valor": 180.23,
            "referencia": "202008",
            "descricao": "Sky",
            "data_vencimento": "2020-8-10"
        }
    }

    context = None
    lambda_handler(event, context)
