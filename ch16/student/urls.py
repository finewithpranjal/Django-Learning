from django.urls import path
from student.views import *
urlpatterns = [
   path('all/', showdata, name='alldata')
]