from django.shortcuts import render, redirect
import pprint
from home.necc_methods import getcallbackurl, getspotipyobject

scope = "user-read-currently-playing user-read-playback-state"


def first(request):
    current_host = request.get_host()

    if current_host.startswith('127.0.0.1') or current_host.startswith('localhost'):
        spo_redirecturl = "http://127.0.0.1:8000/curr_play/callback/"
    else:
        spo_redirecturl = "https://spotify-stats-nvu0.onrender.com/curr_play/callback/"

    request.session['spo_redirecturl'] = spo_redirecturl

    callback_url = getcallbackurl(scope, spo_redirecturl)
    return redirect(callback_url)


def callback(request):
    code = request.GET.get('code')

    if code:
        try:
            spo_redirecturl = request.session.get('spo_redirecturl')
            s = getspotipyobject(scope, spo_redirecturl, code)
            song = s.current_playback()
            pprint.pprint(song)
            return render(request, 'curr_play/curr_play.html', {'song': song})
        except Exception as e:
            print(f"Error in curr_play: {e}")
            return redirect('error')

    return redirect('error')
