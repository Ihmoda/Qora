# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    pass



# User.objects.create(first_name=,last_name=,email=,password=)
# Topic.objects.create(topic=)
# Topic.objects.all().add(users=)
# Question.objects.create(content=,user=)
# Question.objects.all().add(tags=)
# Follow.objects.create(rating=,following=,follower=,question=)#rating 1~5,following True/False
# Answer.objects.create(content=,published=,question=)#published True/False
# AnswerComment(content=,answer=)
# QuestionComment(content=,question=)