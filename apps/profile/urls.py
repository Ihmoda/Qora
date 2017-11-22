from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="profileIndex"),
    url(r'^interests$', views.interests, name="profileInterests"),
    url(r'^interests_add$', views.interests_add, name="profileInterests_add"),
    url(r'^interests_remove$', views.interests_remove, name="profileInterests_remove"),
    url(r'^interests_create$', views.interests_create, name="profileInterests_create"),
    url(r'^', views.index, name="profileIndex"),



]
   