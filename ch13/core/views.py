from django.shortcuts import render

def homepage(req):
    return render(req, 'core/home.html')


def about(req):
    return render(req, 'core/about.html')
  
