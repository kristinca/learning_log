"""URL patterns for learning logs"""

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #     Home page
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.index),
    # Show topics
    url(r'^topics/$', views.topics),
    # url(r'^topics/$', views.topics, name='topics'),
    path(r'Topics', views.topics, name='topics'),
    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path(r'Learning Log', views.index, name='index')
]
