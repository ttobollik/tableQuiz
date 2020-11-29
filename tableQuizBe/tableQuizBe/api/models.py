from django.db import models


class QuizUser(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    picture = models.FileField(upload_to=None, max_length=100, null=True)
    password = models.CharField(max_length=32)


class Question(models.Model):
    # userId = models.CharField(max_length=256)
    userId = models.ForeignKey(
        "QuizUser",
        on_delete=models.CASCADE,
    )
    questionText = models.CharField(max_length=256)
    picture = models.FileField(upload_to=None, max_length=100, null=True)


class Answer(models.Model):
    questionId = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
    )
    answerText = models.CharField(max_length=255)
    answerTrue = models.BooleanField(default=False)
    answerFiftyFifty = models.BooleanField(default=False)
    picture = models.FileField(upload_to=None, max_length=100, null=True)
