#coding=utf-8
from django.conf import settings
from django.conf.urls import url
import views

urlpatterns = [
    url(r'login/',views.login),
    url(r'main/',views.main),
]