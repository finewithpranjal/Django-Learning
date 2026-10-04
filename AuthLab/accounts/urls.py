from django.urls import path
from accounts.views import *

urlpatterns = [
    path('register/', home, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard')
]