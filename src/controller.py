import json

from src import services
from src.decorators import Mapping
from src.https import HttpResponse, CustomJsonEncoder, HttpStatusCode
from src.exceptions import HttpBaseException
from src.models.entrada import Entrada
from src.models.saida import Saida

# __logger = config.logger(__name__)
routes = Mapping()


@routes.get('/entradas')
def get_entradas(event, context):
    service = services.AccountsService()
    try:
        response = service.get_entradas()
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()

    return HttpResponse.success(body=response, json_encoder=CustomJsonEncoder)

@routes.get('/entradas/referencia/{referencia}')
def get_entradas_by_referencia(event, context):
    service = services.AccountsService()
    try:
        response = service.get_entradas_by_referencia(event['pathParameters']['referencia'])
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()
    except KeyError:
        message = "Falta parametro obrigatorio"
        return HttpResponse.build(HttpStatusCode.ERROR, body=message, json_encoder=CustomJsonEncoder)

    return HttpResponse.success(body=response, json_encoder=CustomJsonEncoder)

@routes.post('/entradas')
def post_entradas(event, context):
    service = services.AccountsService()
    try:
        body = event['body'] if type(event['body']) is dict else json.loads(event['body'])
        entrada = Entrada(body)
        service.post_entrada(entrada)
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()

    return HttpResponse.created()

@routes.put('/entradas')
def put_entradas(event, context):
    service = services.AccountsService()
    try:
        body = event['body'] if type(event['body']) is dict else json.loads(event['body'])
        entrada = Entrada(body)
        service.put_entrada(entrada)
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()

    return HttpResponse.no_content()

@routes.delete('/entradas/{id_code}')
def delete_entrada(event, context):
    service = services.AccountsService()
    try:
        service.delete_entrada(event['pathParameters']['id_code'])
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()

    return HttpResponse.no_content()

@routes.get('/saidas')
def get_saidas(event, context):
    service = services.AccountsService()
    try:
        response = service.get_saidas()
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()

    return HttpResponse.success(body=response, json_encoder=CustomJsonEncoder)

@routes.get('/saidas/referencia/{referencia}')
def get_saidas_by_referencia(event, context):
    service = services.AccountsService()
    try:
        response = service.get_saidas_by_referencia(event['pathParameters']['referencia'])
        print(response)
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()
    except KeyError:
        message = "Falta parametro obrigatorio"
        return HttpResponse.build(HttpStatusCode.ERROR, body=message, json_encoder=CustomJsonEncoder)

    return HttpResponse.success(body=response, json_encoder=CustomJsonEncoder)

@routes.post('/saidas')
def post_saidas(event, context):
    service = services.AccountsService()
    try:
        body = event['body'] if type(event['body']) is dict else json.loads(event['body'])
        saida = Saida(body)
        service.post_saida(saida)
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()

    return HttpResponse.created()

@routes.put('/saidas')
def put_saidas(event, context):
    service = services.AccountsService()
    try:
        body = event['body'] if type(event['body']) is dict else json.loads(event['body'])
        saida = Saida(body)
        service.put_saida(saida)
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()

    return HttpResponse.no_content()

@routes.delete('/saidas/{id_code}')
def delete_saidas(event, context):
    service = services.AccountsService()
    try:
        service.delete_saida(event['pathParameters']['id_code'])
    except HttpBaseException as e:
        print(e.get_response())
        return e.get_response()

    return HttpResponse.no_content()
