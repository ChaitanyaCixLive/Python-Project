from django.conf.urls import url, include
from . import views

from news import views

urlpatterns = [
    url(r'^$', views.article_list, name='articles_list'),
]