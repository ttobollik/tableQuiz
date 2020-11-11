from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from tableQuizBe.api import views

router = routers.DefaultRouter()
router.register(r'movies', views.QuestionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
