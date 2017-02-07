from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^users', views.show_users),
    url(r'^login', views.login)
    # url(r'^admin/', admin.site.urls),
]
