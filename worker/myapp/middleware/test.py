from  respondentTable import RespondentTable
from sqs_messaging import SendMessage

table = RespondentTable('results')
table.putItem('Alex', 10)
SendMessage('new-respondent-queue', 'Alex')
table.putItem('Ivan', 8)
SendMessage('new-respondent-queue', 'Ivan')

