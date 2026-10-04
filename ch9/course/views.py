from django.shortcuts import render


def learn_django(req):
    return render(req, 'course/django.html', {'nm': 'Django 6.x'})
