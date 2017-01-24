from django.conf.urls import url
from . import views


app_name = 'music';

urlpatterns = [
    url(r'^$', views.index, name='index'),  #$ means the homepasge for individual app
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')
]
