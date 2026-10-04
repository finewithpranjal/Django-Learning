from django.urls import path
from student.views import *
urlpatterns = [
    path('', home , name='home'),
    # path('profile/<my_id>', profile, name='profile'),
    path('profile/<int:my_id>', profile, name='profile'),
]