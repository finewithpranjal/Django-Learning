from django.urls import path
from course.views import *

urlpatterns = [
    path('dj/', learn_django)
]