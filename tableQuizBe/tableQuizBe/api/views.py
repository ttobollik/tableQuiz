from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import QuizUser, Question, Answer
from .serializers import QuizUserSerializer, QuestionSerializer, AnswerSerializer


class QuizUserViewSet(viewsets.ModelViewSet):
    queryset = QuizUser.objects.all()
    serializer_class = QuizUserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
