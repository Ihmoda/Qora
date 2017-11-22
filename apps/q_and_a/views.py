# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    context = {
        user = User.objects.get(id=request.session['id']),
    }
    
    return render(request, "q_and_a/home.html", context)

def add(request):
    return render(request, "q_and_a/add.html")