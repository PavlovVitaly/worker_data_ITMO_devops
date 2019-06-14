import boto3

class RespondentTable(object):

    _respondent = 'Respondent'
    _number_of_right_answers = 'NumberOfRightAnswers'
    _table = None
    
    def __init__(self, table):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://dynamodb.us-east-1.amazonaws.com")
        self._table = dynamodb.Table(table)

    def putItem(self, respondent, number_of_right_answers):
        self._table.put_item(
        Item={
            self._respondent : respondent,
            self._number_of_right_answers : number_of_right_answers
        })

    def getItem(self, respondent):
        response = self._table.get_item(
        Key={
            self._respondent : respondent
        })
        return response.get('Item', None)

