from django.urls import path
from courses.views import *

urlpatterns = [
    path('dj/', learn_django, name='learn_djanogo'),
    path('fst/', learn_fastapi, name='learn_fastapi' )
]