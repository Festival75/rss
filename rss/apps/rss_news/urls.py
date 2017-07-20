from django.conf.urls import url
from django.contrib import admin
from rss.apps.rss_news import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'post/(?P<id>[0-9]+)/$', views.post, name='post'),
    url(r'signup_user/$', views.signup_user, name='signup_user'),
    url(r'check_username/$', views.check_username, name='check_username'),
]
