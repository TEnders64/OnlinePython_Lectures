from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hobbies$', views.create),
    url(r'^all$', views.all),
]
