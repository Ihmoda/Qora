# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_registration.models import *
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):

    context = {
        "user": User.objects.get(id=request.session['id']),
        "questions": Question.objects.all()
    }
    
    return render(request, "q_and_a/home.html", context)

def add(request):
    if request.method == 'POST' and 'id' in request.session:
        errors = {}
        anonymity = False
        if len(request.POST['newquestion']) < 10:
            errors['addition'] = "Your question must be at least 10 character in length"
            for error in errors:
                messages.error(request, error)
            return redirect(reverse('q_and_a:home'))
        else:
            if 'anonymous' in request.POST:
                anonymity = True
            user = User.objects.get(id=request.session['id'])
            que = Question.objects.create(content=request.POST['newquestion'], anonymity=anonymity, user=user)
            return redirect(reverse('q_and_a:home'))
    else:
        return redirect(reverse('q_and_a:home'))

    return redirect(reverse('login:logIndex'))


def newanswer(request, questionid):
    print "hit route"
    if request.method == 'POST' and 'id' in request.session:
        print "passed check"
        errors = {}
        if len(request.POST['answer']) < 10:
            errors['addition'] = "Your question must be at least 10 character in length"
            for error in errors:
                messages.error(request, error)
            return redirect(reverse('q_and_a:home'))
        else:
            print "passed check"
            question = Question.objects.get(id=questionid)
            Answer.objects.create(content=request.POST['answer'], question=question)
            return redirect(reverse('q_and_a:home'))
    return redirect(reverse('q_and_a:home'))
            

