from django.shortcuts import render
from datetime import datetime, timedelta

def setcookie(req):
    responce = render(req,'student/setcookie.html')
    responce.set_cookie('pay_id', 'y111111')
    return responce


def getcookie(req):
    # pay_id = req.COOKIES['pay_id']
    pay_id = req.COOKIES.get('pay_id', 'No cookie found')
    return render(req, 'student/getcookie.html', {'pay_id': pay_id})
     

def deletecookie(req):
    responce = render(req, 'student/deletecookie.html')
    responce.delete_cookie('pay_id')
    return responce


def setsignedcookie(req):
    responce = render(req, 'student/setsignedcookie.html')
    responce.set_signed_cookie('token', 't123', salt='tk')
    return responce


def getsignedcookie(req):
    token = req.get_signed_cookie('token', salt='tk', default='No cookie found')
    return render(req, 'student/getssignedcookie.html', {'token': token})