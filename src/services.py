from os import environ
from src.services_base import ServiceBaseDynamoDB


class AccountsService(ServiceBaseDynamoDB):

    def __init__(self):
        super().__init__(region='us-east-2')
        self.entradas_table = environ.get('DynamoDBEntradas', 'entradas')
        self.saidas_table = environ.get('DynamoDBSaidas', 'saidas')

    def get_entradas(self):
        return super().get(self.entradas_table)

    def get_entradas_by_referencia(self, referencia):
        return super().get_by_filter(self.entradas_table, 'referencia', int(referencia))

    def post_entrada(self, entrada):
        super().post(self.entradas_table, entrada.get(), 'id_code')

    def put_entrada(self, entrada):
        super().put(self.entradas_table, entrada.get(), 'id_code')

    def delete_entrada(self, id_code):
        item = {"id_code": id_code, "referencia": int(id_code[-6:])}
        super().delete(self.entradas_table, item)

    def get_saidas(self):
        return super().get(self.saidas_table)

    def get_saidas_by_referencia(self, referencia):
        return super().get_by_filter(self.saidas_table, 'referencia', int(referencia))

    def post_saida(self, saida):
        return super().post(self.saidas_table, saida.get(), 'id_code')

    def put_saida(self, saida):
        return super().put(self.saidas_table, saida.get(), 'id_code')

    def delete_saida(self, id_code):
        item = {"id_code": id_code, "referencia": int(id_code[-6:])}
        super().delete(self.saidas_table, item)