from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hobbies$', views.create),
    url(r'^all$', views.all),
    url(r'^hobbies/(?P<hobby_id>\d+)/edit$', views.edit),
    url(r'^hobbies/(?P<hobby_id>\d+)$', views.oneHobby),
    url(r'^hobbies/(?P<hobby_id>\d+)/delete$', views.delete),
]
