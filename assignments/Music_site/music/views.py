from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Musician, Album, Song

def MusicianListView(ListView):
    template_name = 'music/musician_list.html'
    context_object_name = 'Musician_list'

    def get_queryset(self):
       return Musician.objects.all()


def MusicianDetailView(DetailView):
    model = Musician
    template_name = "music/musician.html"

def AlbumDetailView(DetailView):
    model = Album
    template_name = 'music/album.html'

def SongDetailView(DetailView):
    model = Song
    template_name = 'music/song.html'


def home(request):
    return HttpResponse("Hello, world. This is my music site!")

def classical_songs(request):
    return HttpResponse("Hello Classical!")