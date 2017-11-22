# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..login_registration.models import *
# Create your views here.
def index(request):
    if request.session['id'] != None:
        return render(request, "profile/index.html")
    else:
        return redirect(reverse('login:logIndex'))
