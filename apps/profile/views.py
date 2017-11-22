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
            'user':user,
            'questions':Question.objects.all(),
        }
        return render(request, "profile/index.html",context)
    else:
        return redirect(reverse('login:logIndex'))
def interests(request):
    if request.session['id'] != None:
        user = User.objects.get(id=request.session['id'])
        topics=user.interests.all()
        otherTopics=Topic.objects.all().exclude(users=user)
        context={
            'topics':topics,
            'otherTopics':otherTopics,
            'user':user
        }
        return render(request, "profile/interests.html",context)
    else:
        return redirect(reverse('login:logIndex'))
def interests_add(request):
    # Topic.objects.filter(topic='asfdsaf').delete()
    if request.method == 'POST' and 'id' in request.session:
        errors = {}
        user = User.objects.get(id=request.session['id'])
        if 'newTopic' in request.POST:
            if Topic.objects.filter(topic=request.POST['newTopic'] ):
                topic = Topic.objects.get(topic=topicName)
                topic.users.add(user)
            else:
                topic = request.POST['newTopic']   
                newTopic = Topic.objects.create(topic=topic)
                newTopic.users.add(user)
        else:
            #validate topic exists
            topicName = request.POST['topic']   
            topic = Topic.objects.get(topic=topicName)
            topic.users.add(user)
    return redirect(reverse('profile:profileInterests'))
def interests_remove(request):
    #validation later
    if request.method == 'POST' and 'id' in request.session:
        errors = {}
        user = User.objects.get(id=request.session['id'])
        if 'topic' in request.POST:
            topic = Topic.objects.get(topic=request.POST['topic'])
            topic.users.remove(user)
    return redirect(reverse('profile:profileInterests'))
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