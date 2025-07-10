from django.shortcuts import render,redirect
import pprint
from home.necc_methods import getcallbackurl,getspotipyobject

spo_redirecturl="http://127.0.0.1:8000/top_tracks/callback/"
scope = "user-top-read"

def first(request):
    callback_url = getcallbackurl(scope, spo_redirecturl)
    return redirect(callback_url)

def callback(request):
    code = request.GET.get('code')
    if code:
        s = getspotipyobject(scope, spo_redirecturl, code)
        tracks = s.current_user_top_tracks(limit=5)
        pprint.pprint(tracks)
        return render(request, 'top_tracks/top_tracks.html', {'tracks': tracks})
    return None

