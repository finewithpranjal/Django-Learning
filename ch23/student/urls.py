from django.urls import path
from student.views import *
urlpatterns = [
   path('register/', register, name = 'register'),
   path('success/', thankyou, name = 'success'),
]
