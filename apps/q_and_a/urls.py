from django.conf.urls import url
from . import views

  
urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^add', views.add, name="add"),
    url(r'^new/(?P<questionid>\d+)$', views.newanswer, name="newanswer"),
    url(r'^/question/(?P<question_id>\d+)$', views.question, name="question"),
    url(r'^/question/(?P<question_id>\d+)/comment_add$', views.comment_add, name="comment"),
    url(r'^/answer/(?P<answer_id>\d+)/comment_add$', views.answer_comment_add, name="comment"),
]