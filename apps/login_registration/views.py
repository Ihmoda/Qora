from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime

def index(request):
    if not 'id' in request.session:
        request.session['id'] = None
    if not 'name' in request.session:
        request.session['name']=None
    if request.session['id'] != None:
        return redirect ('/friends')
    else:
        return render(request, "pythonBeltApp/index.html")
    
def login(request):
    result = User.objects.valLogin(request.POST)
    if result[0]:
        request.session['id'] = result[1].id
        request.session['name'] = result[1].username
        context={
            "user": result[1]
        }
        return redirect('/friends', context)
    else:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/')

def register(request):
    if request.session['id'] != None:
        return redirect ('/friends')
    else:
        context={
            "max": datetime.today().strftime('%Y-%m-%d')
        }
        return render(request, "pythonBeltApp/registration.html", context)

def process(request):
    result = User.objects.valCreate(request.POST)
    if result[0]:
        request.session['id'] = result[1].id
        request.session['name'] = result[1].username
        return redirect('/friends')
    else:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/register')

def error(request):
    messages.error(request, "This route does not exist")
    return render(request, "pythonBeltApp/error.html")

def logout(request):
    request.session.clear()
    return redirect('/')