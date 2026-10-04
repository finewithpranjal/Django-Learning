from django.shortcuts import render


def checktestcookie(req):
    return render(req, 'student/checktestcookie.html')

def delsession(req):
    if 'fname' in req.session:
        del req.session['fname'] 
    return render(req, 'student/delsession.html')

def deltestcookie(req):
    return render(req, 'student/deltestcookie.html')

def flushsession(req):
    req.session.flush()
    return render(req, 'student/flushsession.html')

def getsession(req):
    first_name = req.session['fname']
    last_name = req.session['lname']
    return render(req, 'student/getsession.html', {'first_name': first_name, 'last_name': last_name})

def setsession(req):
    req.session['fname'] = 'John'
    req.session['lname'] = 'Doe'
    return render(req, 'student/setsession.html')

def settestcookie(req):
    return render(req, 'student/settestcookie.html')

def sessionclear(req):
    return render(req, 'student/sessionclear.html')

def sessionmethodsintemplate(req):
    return render(req, 'student/sessionmethodsintemplate.html')

def sessionmethodsinview(req):
    keys = req.session.keys()
    age = req.session.setdefault('age', 25)
    print(age)
    print(keys)
    return render(req, 'student/sessionmethodsinview.html')