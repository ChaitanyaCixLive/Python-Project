from django.http import HttpResponse
from .models import Album, Song
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


def favourite(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exists")

    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album':album,
            'error_message':"you did not select a valid song",
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})