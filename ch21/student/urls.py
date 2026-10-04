from django.urls import path
from student.views import registeration, address
urlpatterns = [
    path('register/', registeration, name='register'),
    path('address/', address, name='address'),
]