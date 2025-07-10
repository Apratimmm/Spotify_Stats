from django.contrib import admin
from django.urls import path,include
from . import views as v

urlpatterns = [
    path('',v.homepage, name='home'),
    path('curr_play/',include('curr_play.urls')),
    path('rec_play/',include('rec_play.urls')),
    path('user_playlist/',include('user_playlist.urls')),
    path('top_artists/',include('top_artists.urls')),
    path('top_tracks/',include('top_tracks.urls'))
]
