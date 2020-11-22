from django.contrib import admin
from .models import QuizUser, Question, Answer

admin.site.register(QuizUser)
admin.site.register(Question)
admin.site.register(Answer)