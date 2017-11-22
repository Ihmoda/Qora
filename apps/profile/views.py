# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..login_registration.models import *
# Create your views here.
def index(request):
    if request.session['id'] != None:
        user = User.objects.get(id=request.session['id'])
        print user.first_name
        context={
            'user':user
        }
        return render(request, "profile/index.html",context)
    else:
        return redirect(reverse('login:logIndex'))
def interests(request):
    if request.session['id'] != None:
        print 'here'
        user = User.objects.get(id=request.session['id'])
        topics=Topic.objects.all()
        otherTopics=Topic.objects.all()
        context={
            'topics':topics,
            'otherTopics':otherTopics,
            'user':user
        }
        return render(request, "profile/interests.html",context)
    else:
        return redirect(reverse('login:logIndex'))
def interests_add(request):
    if request.method == 'POST' and 'id' in request.session:
        errors = {}
        user = User.objects.get(id=request.session['id'])
        if 'newTopic' in request.POST:
            topic = request.POST['newTopic']       
            newTopic = Topic.objects.create(topic=topic)
            newTopic.users.add(user)
        else:
            pass#simply add topic that was clicked on
    return redirect(reverse('profile:interests'))

    return redirect(reverse('login:logIndex'))
def interests_create(request, questionid):
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
            user = User.objects.get(id=request.session['id'])
            Answer.objects.create(content=request.POST['answer'], question=question, user=user)
            return redirect(reverse('q_and_a:home'))
    return redirect(reverse('q_and_a:home'))