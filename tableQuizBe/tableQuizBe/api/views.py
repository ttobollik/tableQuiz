from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tableQuizBe.api.serializers import QuestionSerializer
from .models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
