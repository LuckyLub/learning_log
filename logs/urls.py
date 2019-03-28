from django.urls import path
from django.conf.urls import url

from logs import views

app_name = 'logs'

urlpatterns = [
    path('', views.topic_overview, name="index"),
    path('new_topic', views.new_topic, name="new_topic"),
    path('topic/<topic>', views.topic, name="topic"),
]

