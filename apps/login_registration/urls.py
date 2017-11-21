from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index), #display login
    url(r'^login$', views.login), #process login form
    url(r'^register$', views.register), #display registration
    url(r'^process$', views.process), #process registration form
    url(r'^', views.error)
]