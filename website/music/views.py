from django.http import HttpResponse
from .models import Album
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()

    context = {
        'all_albums' : all_albums,
    }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exists")

    context = {
        'album': album
    }
    return render(request, 'music/detail.html', context)