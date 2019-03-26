from django.urls import path
from django.conf.urls import url

from logs import views

urlpatterns = [
    path('', views.topic_overview),
    path('topic/<topic>', views.topic),
]
