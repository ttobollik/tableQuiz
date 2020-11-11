from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_author = models.CharField(max_length=30)
    question_category = models.CharField(max_length=30)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer_text = models.CharField(max_length=200)
    answer_correct = models.BooleanField(default=0)
    answer_fifty_fifty = models.BooleanField(default=0)
    answer_comment = models.CharField(max_length=400)
    answer_picture = models.CharField(max_length=200)
