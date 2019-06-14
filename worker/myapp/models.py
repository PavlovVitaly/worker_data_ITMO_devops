from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_right_answer = models.BooleanField()

    def __str__(self):
        return self.text
