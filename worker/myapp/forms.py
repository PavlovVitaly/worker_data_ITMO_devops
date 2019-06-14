from django import forms
from myapp.middleware.Test import *


class LinuxTest1Form(forms.Form):
    name = forms.CharField(label='Your nickname:', max_length=100, strip=True)
    def __init__(self, *args, **kwargs):
        super(LinuxTest1Form, self).__init__(*args, **kwargs)
        test = TestContent('Linux test 1')
        cnt = 0
        for q in test.questions:
            self.fields['question-' + str(cnt+1)] = forms.CharField(label= q.text, widget=forms.RadioSelect(choices=q.options))
            cnt += 1
