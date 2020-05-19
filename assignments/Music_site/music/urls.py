from django.urls import path

from . import views

urlpatterns = [
  path('', views.MusicianListView, name='musicians'),
  path('musician/<int:pk>/', views.MusicianDetailView, name='musician'),
  path('album/<int:pk>/album/', views.AlbumDetailView, name='album'),
  path('song/<int:pk>/song/', views.SongDetailView, name='song'),
]