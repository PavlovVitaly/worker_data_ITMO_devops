from myapp.middleware.StatisticsTable import StatisticsTable

def GetStatistics(table_name, num_of_elems=0):
    stat = StatisticsTable(table_name).getAllItems()
    res = {}
    for i in range(1,num_of_elems+1):
        res[i] = 0
    for item in stat:
        res[item['NumberOfRightAnswers']] = item['NumberOfRespondents']
    return res
