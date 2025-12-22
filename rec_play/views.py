from django.shortcuts import render, redirect
import pprint
from home.necc_methods import getcallbackurl, getspotipyobject

scope = "user-read-recently-played"


def first(request):
    request.session['limit'] = request.GET.get('limit', 5)
    current_host = request.get_host()

    if current_host.startswith('127.0.0.1') or current_host.startswith('localhost'):
        spo_redirecturl = "http://127.0.0.1:8000/rec_play/callback/"
    else:
        spo_redirecturl = "https://spotify-stats-nvu0.onrender.com/rec_play/callback/"

    request.session['spo_redirecturl'] = spo_redirecturl

    callback_url = getcallbackurl(scope, spo_redirecturl)
    return redirect(callback_url)


def callback(request):
    code = request.GET.get('code')
    limit = request.session.get('limit', 5)

    if code:
        try:
            spo_redirecturl = request.session.get('spo_redirecturl')
            s = getspotipyobject(scope, spo_redirecturl, code)
            songs = s.current_user_recently_played(limit=limit)
            pprint.pprint(songs)
            return render(request, 'rec_play/rec_play.html', {'songs': songs})
        except Exception as e:
            print(f"Error in rec_play: {e}")
            return redirect('error')

    return redirect('error')
