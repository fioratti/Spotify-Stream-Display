import os
import json
import spotipy
import spotipy.util as util
from env import *

token = util.prompt_for_user_token(SPOTIFY_USERNAME, scope='user-read-playback-state', client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_SECRET_ID, redirect_uri=SPOTIFY_REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)

    # RETRIEVES SONG NAME
    print(sp.currently_playing()['item']['name'])

    # RETRIEVES ARTIST NAME
    print(sp.currently_playing()['item']['artists'][0]['name'])

    # RETRIEVES ALBUM NAME
    print(sp.currently_playing()['item']['album']['name'])

else:
    print('Cannot Retrieve Token For ' + SPOTIFY_USERNAME)