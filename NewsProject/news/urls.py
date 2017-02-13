from django.conf.urls import url, include
from . import views

from news import views

urlpatterns = [
    url(r'^$', views.articles_list, name='articles_list'),
    url(r'^feeds/', views.feeds_list, name='feeds_list'),
]