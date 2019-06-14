import boto3

class StatisticsTable(object):

    _number_of_right_answers = 'NumberOfRightAnswers'
    _number_of_respondents = 'NumberOfRespondents'
    _table = None

    def __init__(self, table):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://dynamodb.us-east-1.amazonaws.com")
        self._table = dynamodb.Table(table)

    def getAllItems(self):
        response = self._table.scan()
        return response.get('Items', None)

    def putItem(self, number_of_right_answers, number_of_respondents):
        self._table.put_item(
        Item={
            self._number_of_right_answers : number_of_right_answers,
            self._number_of_respondents : number_of_respondents
        })

    def getItem(self, number_of_right_answers):
        response = self._table.get_item(
        Key={
            self._number_of_right_answers : number_of_right_answers
        })
        return response.get('Item', None)
