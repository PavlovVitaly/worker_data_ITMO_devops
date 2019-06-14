from myapp.models import *
  
class TestContent():
    name = None
    questions = []

    def __init__(self, name_of_test):
        test_obj = Test.objects.get(name = name_of_test)
        self.name = test_obj.name
        q = Question.objects.filter(test = test_obj)
        self.questions = list(map(QuestionContent, q))


class QuestionContent():
    text = None
    options = None

    def __init__(self, question_obj):
        self.text = question_obj.text
        opt = Choice.objects.filter(question = question_obj)
        self._formDictOfOptions(opt)

    def _formDictOfOptions(self, options):
        self.options = []
        for item in options:
            self.options.append((item.id, item.text))
