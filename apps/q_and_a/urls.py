from django.conf.urls import url
from . import views

  
urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^add', views.add, name="add"),
    url(r'^new/(?P<questionid>\d+)$', views.newanswer, name="newanswer")
]