from django.shortcuts import render

def home(req):
    return render(req, 'student/home.html')

def profile(req, my_id):
    student = {'id': my_id}
    return render(req, 'student/profile.html', student)