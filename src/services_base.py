import boto3

from boto3.dynamodb.conditions import Attr
from src.commons import config
from src.exceptions import HttpBaseException
from src.https import HttpResponse, HttpStatusCode


class ServiceBaseDynamoDB:

    def __init__(self, region):
        self.__logger = config.logger(__name__)
        self.dynamodb = boto3.resource('dynamodb', region_name=region)

    def get(self, table_name):
        try:
            table = self.dynamodb.Table(table_name)
            results = table.scan()

            return results
        except Exception as err:
            raise HttpBaseException(HttpResponse.bad_request(), {"error": err.args[0]})

    def get_by_filter(self, table_name, filter_name, filter):
        try:
            table = self.dynamodb.Table(table_name)
            results = table.scan(
                FilterExpression=Attr(filter_name).eq(filter)
            )

            return results
        except Exception as err:
            raise HttpBaseException(HttpResponse.bad_request(), {"error": err.args[0]})

    def __put_base(self, table_name, obj, condition):
        try:
            table = self.dynamodb.Table(table_name)

            results = table.put_item(
                Item=obj,
                ConditionExpression=condition
            )

            status_code = results['ResponseMetadata']['HTTPStatusCode']
            if status_code != HttpStatusCode.OK.value:
                raise HttpBaseException(HttpResponse.build(status_code), results)
        except Exception as err:
            raise HttpBaseException(HttpResponse.bad_request(), {"error": err.args[0]})

    def put(self, table_name, obj, key):
        condition = 'attribute_exists(' + key + ')'
        self.__put_base(table_name, obj, condition)

    def post(self, table_name, obj, key):
        condition = 'attribute_not_exists(' + key + ')'
        self.__put_base(table_name, obj, condition)

    def delete(self, table_name, item):
        try:
            table = self.dynamodb.Table(table_name)

            results = table.delete_item(
                Key=item
            )

            status_code = results['ResponseMetadata']['HTTPStatusCode']
            if status_code != HttpStatusCode.OK.value:
                raise HttpBaseException(HttpResponse.build(status_code), results)
        except Exception as err:
            raise HttpBaseException(HttpResponse.bad_request(), {"error": err.args[0]})
