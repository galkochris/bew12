from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Musician, Album, Song

class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'
    context_object_name = 'Musicians'

def musician_detail(request, musician_id):
    albums = Album.objects.filter(artist__id=musician_id)
    musician = Musician.objects.get(id=musician_id)
    
    context = {
        'albums': albums,
        'musician': musician
    }
    return render(request, 'musician.html', context)

def album_detail(request, album_id):
    albums = Album.objects.get(id=album_id)
    songs = Song.objects.filter(album=album_id)

    context = {
        'albums': albums, 
        'songs': songs
    }
    return render(request, 'album.html', context)

def song_detail(request, song_id):
    songs = Song.objects.get(id=song_id)

    context = {
        'song' : songs
    }
    return render(request, 'song.html', context)


def home(request):
    return HttpResponse("Hello, world. This is my music site!")

def classical_songs(request):
    return HttpResponse("Hello Classical!")