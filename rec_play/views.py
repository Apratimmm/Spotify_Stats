from django.shortcuts import render,redirect
import pprint
from home.necc_methods import getcallbackurl,getspotipyobject

spo_redirecturl="https://spotify-stats-nvu0.onrender.com/rec_play/callback/"
scope = "user-read-recently-played"

def first(request):
    request.session['limit']=request.GET.get('limit',5)
    callback_url= getcallbackurl(scope,spo_redirecturl)
    return redirect(callback_url)


def callback(request):
        code = request.GET.get('code')
        limit = request.session.get('limit')
        if code:
            s = getspotipyobject(scope,spo_redirecturl,code)
            songs = s.current_user_recently_played(limit=limit)
            pprint.pprint(songs)
            return render(request, 'rec_play/rec_play.html', {'songs': songs})
        return None
