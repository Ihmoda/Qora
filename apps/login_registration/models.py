# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def valCreate(self, postData):
        errors = []
        numResults = User.objects.filter(email=postData['email'])
        if len(numResults) > 0:
            errors.append("Unable to register: email is taken")
            return (False, errors)
        results = User.objects.filter(username=postData['username'])
        if len(results)>0:
            errors.append("Unable to register: Username is taken")
            return (False, errors)

        if len(postData['fName'])<1 and len(postData['lName'])<1 and len(postData['username'])<1 and len(postData['email'])<1 and len(postData['birthdate'])<1 and len(postData['pwd'])<1:
            errors.append("Please fill out the form to register")
            return (False, errors)
        if len(postData['fName'])<2:
            errors.append("First name is required and must be at least 2 characters")
        elif not NAME_REGEX.match(postData['fName']):
            errors.append("Invalid first name")
        if len(postData['lName'])<2:
            errors.append("Last name is required and must be at least 2 characters")
        elif not NAME_REGEX.match(postData['lName']):
            errors.append("Invalid last name")
        if len(postData['username'])<2:
            errors.append("Username is required and must be at least 2 characters")
        elif not USERNAME_REGEX.match(postData['username']):
            errors.append("Invalid username")
        if postData['email'] == "":
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid email")
        if postData['birthdate'] == "":
            errors.append("Birthdate is required")
        else:
            bday = datetime.strptime(postData['birthdate'], '%Y-%m-%d')
            today=datetime.today()
            if (today-bday).days/365<18:
                errors.append("Unable to register: User must be 18 years or older")
        if postData['pwd'] == "":
            errors.append("Password is required")
        elif not PASSWORD_REGEX.match(postData['pwd']):
            errors.append("Invalid password")
        elif len(postData['pwd'])>15:
            errors.append("Password is too long")
        if postData['pwd'] != postData['confirm']:
            errors.append("Password does not match password confirmation")
        if len(errors) == 0:
            hashed = bcrypt.hashpw(postData['pwd'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name = postData['fName'], last_name = postData['lName'],username = postData['username'], email = postData['email'],birthday = bday, password = hashed)
            return (True, user)
        else:
            return (False, errors)

    # IF THERE IS EXTRA TIME, ALLOW USERS TO LOGIN USING EMAIL OR USERNAME
    def valLogin(self,postData):
        errors=[]
        if postData['username'] == "" and postData['pwd'] == "":
            errors.append("Please fill out the form to login")
            return (False, errors)
        if postData['username'] == "":
            errors.append("Username is required")
        if postData['pwd'] == "":
            errors.append("Password is required")
        if not User.objects.filter(username = postData['username']):
            errors.append("Incorrect username")
        else:
            password = User.objects.filter(username = postData['username'])[0].password
            if bcrypt.hashpw(postData['pwd'].encode(), password.encode()) != password:
                errors.append("Incorrect password")
        if len(errors)!=0:
            return (False, errors)
        else:
            user = self.get(username = postData['username'])
            return (True, user)
    
    def valUserRoute(self, id):
        errors=[]
        user = User.objects.filter(id=id)
        if len(user)==0:
            errors.append("This user does not exist")
            return(False, errors)
        else:
            return (True, errors)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

class Topic(models.Model):
    topic = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name="interests")

class Question(models.Model):
    content = models.TextField()
    anonymity = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Topic, related_name="questions")
    user = models.ForeignKey(User, related_name = "questions")

class Follow(models.Model):
    rating = models.IntegerField()
    following = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    follower = models.ForeignKey(User, related_name="questions_followed")
    question = models.ForeignKey(Question, related_name="followers")

class Answer(models.Model):
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, related_name="answers")

class AnswerComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    answer = models.ForeignKey(Answer, related_name="comments")

class QuestionComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, related_name="comments")




