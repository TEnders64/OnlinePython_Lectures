from django.conf.urls import url
from . import views
#url that is coming in:
# /users24
urlpatterns = [
    url(r'^$', views.index), # /
    url(r'^users$', views.create), # /users
]
