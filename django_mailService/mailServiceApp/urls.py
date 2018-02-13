from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^$', index, name="index" ),
	url(r'^about/$', about, name="about"),
	url(r'^contact/$', contact_us, name="contact"),
	url(r'^clear/$', clear, name="clear")
    
]
