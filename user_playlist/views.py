from django.http import HttpResponse
from django.shortcuts import render,redirect
import pprint
from home.necc_methods import getcallbackurl,getspotipyobject

spo_redirecturl="http://127.0.0.1:8000/user_playlist/callback/"
scope = "playlist-read-private"

def first(request):
    callback_url = getcallbackurl(scope, spo_redirecturl)
    return redirect(callback_url)

def callback(request):
    code = request.GET.get('code')
    if code:
        s = getspotipyobject(scope, spo_redirecturl, code)
        playlist= s.current_user_playlists()
        pprint.pprint(playlist)
        return render(request,'user_playlist/user_playlist.html',{'playlist':playlist})

