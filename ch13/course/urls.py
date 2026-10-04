from django.urls import path
from course.views import *
urlpatterns = [
    path('django/', heydjango, name='django'),
    path('python/', heypython, name='python'),
]