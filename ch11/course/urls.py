from django.urls import path
from course.views import *
urlpatterns = [
    path('Django/', heydjango),
    path('Python/', heypython),
]