import json

from decimal import *
from src.commons.utils import normalize
from src.https import HttpResponse
from src.exceptions import HttpBaseException


class Saida:

    def __init__(self, obj: dict):
        try:
            code = normalize('C' + str.upper((obj['descricao'][::2] + obj['referencia']).replace(' ', '')))
            self.id_code = obj.get('id_code', code)
            self.referencia = int(obj['referencia'])
            self.valor = float(obj['valor'])
            self.descricao = str(obj['descricao'])
            self.data_vencimento = str(obj['data_vencimento'])
            self.data_pagamento = obj.get('data_pagamento', None)
        except ValueError as err:
            raise HttpBaseException(HttpResponse.error(), 'models.Saida: ' + err.args[0])
        except KeyError as err:
            raise HttpBaseException(HttpResponse.error(), 'models.Saida: ' + err.args[0])

    def __str__(self):
        return json.dumps({
            "id_code": self.id_code,
            "referencia": self.referencia,
            "valor": self.valor,
            "descricao": self.descricao,
            "data_vencimento": self.data_vencimento,
            "data_pagamento": self.data_pagamento
        })

    def get(self):
        data: dict = {"id_code": self.id_code, "referencia": self.referencia, "valor": self.valor,
                      "descricao": self.descricao, "data_vencimento": self.data_vencimento}

        if self.data_pagamento:
            data["data_pagamento"] = self.data_pagamento

        return json.loads(json.dumps(data), parse_float=Decimal)
