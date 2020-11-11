from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_author',
                  'question_category', 'answer_a', 'answer_b', 'answer_c', 'answer_d']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'answer_correct',
                  'answer_fifty_fifty', 'answer_comment', 'answer_picture']
