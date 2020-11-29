from django.contrib.auth.models import User, Group
from .models import QuizUser, Question, Answer
from rest_framework import serializers


class QuizUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = QuizUser
        fields = ['id', 'username', 'email', 'picture', 'password']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'userId', 'questionText', 'picture']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'questionId', 'answerText', 'answerTrue', 'answerFiftyFifty', 'picture']