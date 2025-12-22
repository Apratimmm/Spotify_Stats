from django.shortcuts import render, redirect
import pprint
from home.necc_methods import getcallbackurl, getspotipyobject

scope = "user-top-read"


def first(request):
    current_host = request.get_host()

    if current_host.startswith('127.0.0.1') or current_host.startswith('localhost'):
        spo_redirecturl = "http://127.0.0.1:8000/top_tracks/callback/"
    else:
        spo_redirecturl = "https://spotify-stats-nvu0.onrender.com/top_tracks/callback/"

    request.session['spo_redirecturl'] = spo_redirecturl

    callback_url = getcallbackurl(scope, spo_redirecturl)
    return redirect(callback_url)


def callback(request):
    code = request.GET.get('code')

    if code:
        try:
            spo_redirecturl = request.session.get('spo_redirecturl')
            s = getspotipyobject(scope, spo_redirecturl, code)
            tracks = s.current_user_top_tracks(limit=5)
            pprint.pprint(tracks)
            return render(request, 'top_tracks/top_tracks.html', {'tracks': tracks})
        except Exception as e:
            print(f"Error in top_tracks: {e}")
            return redirect('error')

    return redirect('error')


