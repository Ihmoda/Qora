from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime
from django.core.urlresolvers import reverse

def index(request):
    if not 'id' in request.session:
        request.session['id'] = None
    if not 'name' in request.session:
        request.session['name']=None
    if request.session['id'] != None:
        # CHANGE TO CORRECT ROUTE
        return HttpResponseRedirect(reverse('q_and_a:home'))
    else:
        return render(request, "login_registration/index.html")
    
def login(request):
    result = User.objects.valLogin(request.POST)
    if result[0]:
        request.session['id'] = result[1].id
        request.session['name'] = result[1].username
        context={
            "user": result[1]
        }
        # CHANGE TO CORRECT ROUTE
        return HttpResponseRedirect(reverse('q_and_a:home', context))
    else:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/')

def register(request):
    if request.session['id'] != None:
        # CHANGE TO CORRECT ROUTE
        return HttpResponseRedirect(reverse('q_and_a:home'))
    else:
        context={
            "max": datetime.today().strftime('%Y-%m-%d')
        }
        return render(request, "login_registration/registration.html", context)

def process(request):
    result = User.objects.valCreate(request.POST)
    if result[0]:
        request.session['id'] = result[1].id
        request.session['name'] = result[1].username
        # CHANGE TO CORRECT ROUTE IN SEPARATE APP
        return HttpResponseRedirect(reverse('q_and_a:home'))
    else:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/register')

def error(request):
    messages.error(request, "This route does not exist")
<<<<<<< HEAD
    return render(request, "login_registration/error.html")
=======
    return render(request, "pythonBeltApp/error.html")

def logout(request):
    request.session.clear()
    return redirect('/')
>>>>>>> f406e79d4a3038d1c6c1ecbcd1283caef55c6c13
