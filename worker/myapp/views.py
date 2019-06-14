from django.shortcuts import render
from .forms import LinuxTest1Form
from myapp.middleware.ResultProcessing import ProcessTest
from myapp.middleware.ResultProcessing import FormResultOfTest
from myapp.middleware.StatisticsProcessing import GetStatistics
from myapp.models import Test, Question

# Create your views here.
def hello(request):
       return render(request, 'hello.html', {})

def get_linux_test_1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LinuxTest1Form(request.POST)
        res = ProcessTest(request.POST, 'results', 'new-respondent-queue')
        return render(request, 'results.html', FormResultOfTest('Linux test 1', 'Linux test 1', res))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LinuxTest1Form()

    return render(request, 'linux_test_1.html', {'form': form})

def get_linux_test_1_statistics(request):
    cnt = Question.objects.filter(test=Test.objects.get(name = 'Linux test 1')).count()
    stat = GetStatistics('statistics', cnt)
    return render(request, 'statistics.html', {'title_of_page': 'Linux test 1 statistics', 'title_of_chart': 'Linux test 1 statistics', 'statistics': stat})
