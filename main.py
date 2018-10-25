import tkinter as tk
import spotipy
import spotipy.util as util
from env import *

# TODO Optimize code to compile into executable

token = util.prompt_for_user_token(SPOTIFY_USERNAME, scope='user-read-playback-state', client_id=SPOTIFY_CLIENT_ID,
                                   client_secret=SPOTIFY_SECRET_ID, redirect_uri=SPOTIFY_REDIRECT_URI)

widget = tk.Tk()

if token:

    sp = spotipy.Spotify(auth=token)

    # INITIALIZATION OF WIDGET
    check_new_song = sp.currently_playing()['item']['name']

    # RETRIEVES SONG NAME
    song_name = sp.currently_playing()['item']['name']

    # RETRIEVES ARTIST NAME
    artist_name = sp.currently_playing()['item']['artists'][0]['name']

    output_str = tk.StringVar()

    output_str.set('Current Song:\n%s\n%s' % (song_name, artist_name))

    spotify_labels = tk.Label(widget, textvariable=output_str, bg='#00ff00', justify='left',
                              font='Courier 44 bold', fg='white')

    spotify_labels.pack()

    widget.update()

    while True:
        if check_new_song != sp.currently_playing()['item']['name']:

            # CLEARS WIDGET TEXT FOR SONG UPDATE
            spotify_labels.destroy()

            check_new_song = sp.currently_playing()['item']['name']

            # RETRIEVES SONG NAME
            song_name = sp.currently_playing()['item']['name']

            # RETRIEVES ARTIST NAME
            artist_name = sp.currently_playing()['item']['artists'][0]['name']

            output_str = tk.StringVar()

            output_str.set('Current Song:\n%s\n%s' % (song_name, artist_name))

            spotify_labels = tk.Label(widget, textvariable=output_str, bg='#00ff00', justify='left',
                                      font='Courier 44 bold', fg='white')

            spotify_labels.pack()

            widget.update()

else:
    print('Cannot Retrieve Token For ' + SPOTIFY_USERNAME)