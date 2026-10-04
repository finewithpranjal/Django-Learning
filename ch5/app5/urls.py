from django.contrib import admin
from django.urls import path
from app5.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('app5/', myapp5, name='myapp5'),
]
