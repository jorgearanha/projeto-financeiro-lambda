import json

from decimal import *
from src.https import HttpResponse
from src.exceptions import HttpBaseException


class Entrada:

    def __init__(self, obj: dict):
        try:
            code = str.upper((obj['descricao'][::3] + str(obj['referencia'])).replace(' ', ''))
            self.id_code = obj.get('id_code', code)
            self.referencia = int(obj['referencia'])
            self.valor = float(obj['valor'])
            self.descricao = str(obj['descricao'])
            self.data_recebimento = obj.get('data_recebimento', None)
        except ValueError as err:
            raise HttpBaseException(HttpResponse.error(), 'models.Entrada: ' + err.args[0])
        except KeyError as err:
            raise HttpBaseException(HttpResponse.error(), 'models.Entrada: ' + err.args[0])

    def __str__(self):
        return json.dumps({
            "id_code": self.id_code,
            "referencia": self.referencia,
            "valor": self.valor,
            "descricao": self.descricao,
            "data_recebimento": self.data_recebimento
        })

    def get(self):
        data: dict = {"id_code": self.id_code, "referencia": self.referencia, "valor": self.valor,
                      "descricao": self.descricao}

        if self.data_recebimento:
            data["data_recebimento"] = self.data_recebimento

        return json.loads(json.dumps(data), parse_float=Decimal)
