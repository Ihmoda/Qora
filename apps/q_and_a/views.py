# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_registration.models import *
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.
def index(request):

    context = {
        "user": User.objects.get(id=request.session['id']),
        "questions": Question.objects.all(),
        "answers": Answer.objects.all()
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
        errors = {}
        if len(request.POST['answer']) < 10:
            errors['addition'] = "Your answer must be at least 10 character in length"
            for error in errors:
                messages.error(request, error)
            return redirect(reverse('q_and_a:home'))
        else:
            print "passed check"
            
            question = Question.objects.get(id=questionid)
            print question.id

            user = User.objects.get(id=request.session['id'])
            answer=Answer.objects.create(content=request.POST['answer'], question=question, user=user)
            print user.id
            print answer.id
            return redirect(reverse('q_and_a:home'))
    return redirect(reverse('q_and_a:home'))
def question(request,question_id):
    question=Question.objects.get(id=question_id)
    context = {
        "user": User.objects.get(id=request.session['id']),
        "questions": [question],
        "answers": Answer.objects.filter(question=question),
        # 'QuestionComments':Question.objects.questioncomments.all(),
    }
      
    return render(request, "q_and_a/question.html", context)      

def comment_add(request,question_id):
    print 'comment_add'
    if request.method == 'POST' and 'id' in request.session:
        errors = {}
        print 'first if'
        if len(request.POST['comment']) < 10:
            print 'here1'
            errors['addition'] = "Your comment must be at least 10 character in length"
            for error in errors:
                messages.error(request, error)
            return redirect(reverse('q_and_a:home'))
        else:
            print 'here2'
            user = User.objects.get(id=request.session['id'])
            que=Question.objects.get(id=question_id)
            comment = QuestionComment.objects.create(content=request.POST['comment'], user=user,question=que)
            return redirect(reverse('q_and_a:home'))
    else:
        print 'not here'
        return redirect(reverse('q_and_a:home'))

    return redirect(reverse('login:logIndex'))
def answer_comment_add(request,answer_id):
    print 'comment_add'
    if request.method == 'POST' and 'id' in request.session:
        errors = {}
        print 'first if'
        if len(request.POST['comment']) < 10:
            print 'here1'
            errors['addition'] = "Your comment must be at least 10 character in length"
            for error in errors:
                messages.error(request, error)
            return redirect(reverse('q_and_a:home'))
        else:
            print 'here2'
            user = User.objects.get(id=request.session['id'])
            ans=Answer.objects.get(id=answer_id)
            comment = AnswerComment.objects.create(content=request.POST['comment'], user=user,answer=ans)
            return redirect(reverse('q_and_a:home'))
    else:
        print 'not here'
        return redirect(reverse('q_and_a:home'))

    return redirect(reverse('login:logIndex'))