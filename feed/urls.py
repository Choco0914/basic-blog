"""feed application url 정의"""
from django.urls import include, re_path
from . import views

app_name = 'feed'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
]
