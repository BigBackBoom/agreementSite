from django.conf.urls import include, url
from django.contrib import admin
from . import views 

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signup$', views.signup, name='signup'),
]
