from myapp.models import Choice
from myapp.middleware.ResultOfTest import ResultOfTest
from datetime import datetime
import hashlib
from  myapp.middleware.RespondentTable import RespondentTable
from myapp.middleware.SqsMessaging import SendMessage
import socket

def FormResultOfTest(title, header, result):
    return {"title": title, "header_of_test": header, "res": result, "hostname": socket.gethostname()}

def ProcessTest(fields, db_name, name_of_queue):
    res = ValidateTest(fields) 
    WriteResultsToDb(db_name, res)
    SendMessageToSqs(name_of_queue, res.name)
    return res

def ValidateTest(fields):
    user_name = GetUserName(fields)
    cnt = 1
    num_of_right_answers = 0
    while cnt > 0:
        opt_id = fields.get('question-'+str(cnt))
        if opt_id == None: break
        if Choice.objects.get(id=opt_id).is_right_answer: num_of_right_answers+=1
        cnt+=1
    return ResultOfTest(user_name, num_of_right_answers)

def GetUserName(fields):
    user_name = fields.get('name')
    user_name += ' ' + hashlib.sha1(bytes( (user_name+str(datetime.now())), 'utf-8')).hexdigest()
    return user_name

def WriteResultsToDb(db_name, result_of_test):
    table = RespondentTable(db_name)
    table.putItem(result_of_test.name, result_of_test.num_of_right_answers)

def SendMessageToSqs(name_of_queue, message):
    SendMessage(name_of_queue, message)
