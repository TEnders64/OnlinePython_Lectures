from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<user>\w+)/(?P<article>.+)/(?P<date>.+)$', views.whoa),
	url(r'^(\w+)', views.show),
	url(r'^(?P<id>\d+)$', views.show),
	url(r'^$', views.index),
]
