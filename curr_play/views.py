from django.shortcuts import render,redirect
import pprint
from home.necc_methods import getcallbackurl,getspotipyobject

spo_redirecturl="http://127.0.0.1:8000/curr_play/callback/"
scope = "user-read-currently-playing user-read-playback-state"

def first(request):
    callback_url = getcallbackurl(scope, spo_redirecturl)
    return redirect(callback_url)


def callback(request):
    code = request.GET.get('code')
    if code:
        s = getspotipyobject(scope,spo_redirecturl,code)
        song = s.current_playback()
        pprint.pprint(song)
        return render(request, 'curr_play/curr_play.html', {'song': song})
    return None