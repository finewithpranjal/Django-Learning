from django.urls import path
from skills.views import *

urlpatterns = [
    path('dj/', showdj, name='show_dj')
]