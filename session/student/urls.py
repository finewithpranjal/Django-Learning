from django.urls import path
from student.views import *
urlpatterns = [
    path('checktestcookie/', checktestcookie),
    path('dels/', delsession),
    path('deltestcookie/', deltestcookie),
    path('flush/', flushsession),
    path('gets/', getsession),
    path('sets/', setsession),
    path('settestcookie/', settestcookie),
    path('sessionclear/', sessionclear),
    path('sessionmethodsintemplate/', sessionmethodsintemplate),
    path('inview/', sessionmethodsinview),
]
