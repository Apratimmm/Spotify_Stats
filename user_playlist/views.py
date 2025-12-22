from django.http import HttpResponse
from django.shortcuts import render, redirect
import pprint
from home.necc_methods import getcallbackurl, getspotipyobject

scope = "playlist-read-private"


def first(request):
    current_host = request.get_host()

    if current_host.startswith('127.0.0.1') or current_host.startswith('localhost'):
        spo_redirecturl = "http://127.0.0.1:8000/user_playlist/callback/"
    else:
        spo_redirecturl = "https://spotify-stats-nvu0.onrender.com/user_playlist/callback/"

    request.session['spo_redirecturl'] = spo_redirecturl

    callback_url = getcallbackurl(scope, spo_redirecturl)
    return redirect(callback_url)


def callback(request):
    code = request.GET.get('code')

    if code:
        try:
            spo_redirecturl = request.session.get('spo_redirecturl')
            s = getspotipyobject(scope, spo_redirecturl, code)
            playlist = s.current_user_playlists()
            pprint.pprint(playlist)
            return render(request, 'user_playlist/user_playlist.html', {'playlist': playlist})
        except Exception as e:
            print(f"Error in user_playlist: {e}")
            return redirect('error')

    return redirect('error')


