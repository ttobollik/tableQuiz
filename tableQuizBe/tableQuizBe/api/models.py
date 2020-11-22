from django.db import models

class QuizUser(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    picture = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class Question(models.Model):
    userId = models.CharField(max_length=32)
    questionText = models.CharField(max_length=256)
    picture = models.CharField(max_length=32)


class Answer(models.Model):
    questionId = models.CharField(max_length=256)
    answerText = models.CharField(max_length=255)
    answerTrue = models.BooleanField(default=False)
    answerFiftyFifty = models.BooleanField(default=False)
    picture = models.CharField(max_length=32)
