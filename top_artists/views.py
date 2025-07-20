from django.shortcuts import render,redirect
import pprint
from home.necc_methods import getcallbackurl,getspotipyobject

spo_redirecturl="https://spotify-stats-nvu0.onrender.com/top_artists/callback/"
scope = "user-top-read"

def first(request):
    callback_url = getcallbackurl(scope, spo_redirecturl)
    return redirect(callback_url)

def callback(request):
    code = request.GET.get('code')
    if code:
        s = getspotipyobject(scope, spo_redirecturl, code)
        artist = s.current_user_top_artists(limit=5)
        pprint.pprint(artist)
        return render(request, 'top_artists/top_artists.html', {'artist': artist})
    return None
