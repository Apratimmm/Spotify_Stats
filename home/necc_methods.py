import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings as st

spo_clientid=st.SPOTIFY_CLIENT_ID
spo_clientpw=st.SPOTIFY_CLIENT_SECRET

def getcallbackurl(scope,spo_redirecturl):
    auth = SpotifyOAuth(client_id=spo_clientid, client_secret=spo_clientpw, scope=scope, redirect_uri=spo_redirecturl)
    callback_url = auth.get_authorize_url()
    return callback_url

def getspotipyobject(scope,spo_redirecturl,code):
    auth = SpotifyOAuth(client_id=spo_clientid, client_secret=spo_clientpw, scope=scope, redirect_uri=spo_redirecturl)
    token_info = auth.get_access_token(code)
    access_token = token_info['access_token']
    s = spotipy.Spotify(auth=access_token)
    return s