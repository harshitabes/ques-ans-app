from django.db import models


# Create your models here.
class Question(models.Model):
    ques_statement = models.CharField(max_length=1000)

    def __str__(self):
        return f'id: {self.id} ques: {self.ques_statement}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans_statement = models.CharField(max_length=1000)

