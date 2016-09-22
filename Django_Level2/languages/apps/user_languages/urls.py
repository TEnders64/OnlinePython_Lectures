from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register_user$', views.register, name='register'),
    url(r'^login_user$', views.login, name='login')
]
