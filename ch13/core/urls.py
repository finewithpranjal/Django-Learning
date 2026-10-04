
from django.urls import path
from core.views import *
urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
]