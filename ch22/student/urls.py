from django.urls import path
from student.views import demo_form
urlpatterns = [
    path('demo', demo_form, name = 'demo_form')
]