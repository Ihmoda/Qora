from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='logIndex'), #display login
    url(r'^login$', views.login), #process login form
    url(r'^register$', views.register, name='logReg'), #display registration
    url(r'^process$', views.process), #process registration form
    url(r'^logout$', views.logout, name="logout"),
    # url(r'^', views.error),
]