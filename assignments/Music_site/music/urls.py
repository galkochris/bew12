from django.urls import path

from . import views

urlpatterns = [
  path('', views.MusicianListView.as_view(), name='musicians'),
  path('musician/<int:musician_id>/', views.musician_detail, name='musician_detail'),
  path('album/<int:album_id>/album/', views.album_detail, name='album_detail'),
  path('song/<int:song_id>/song/', views.song_detail, name='song_detail'),
]