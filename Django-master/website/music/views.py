from django.http import HttpResponse
from django.template import loader
from music.models import Album
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums
    }

    # return HttpResponse(template.render(context, request))

    return render(request, 'music/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExits:
        raise Http404("Album does not exists")
    return render(request, 'music/details.html', {'album' : album})
