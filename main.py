import tkinter as tk
import spotipy
import spotipy.util as util
from env import *

token = util.prompt_for_user_token(SPOTIFY_USERNAME, scope='user-read-playback-state', client_id=SPOTIFY_CLIENT_ID,
                                   client_secret=SPOTIFY_SECRET_ID, redirect_uri=SPOTIFY_REDIRECT_URI)

widget = tk.Tk()

if token:

    sp = spotipy.Spotify(auth=token)

    # RETRIEVES SONG NAME
    print(sp.currently_playing()['item']['name'])
    song_name = sp.currently_playing()['item']['name']

    # RETRIEVES ARTIST NAME
    print(sp.currently_playing()['item']['artists'][0]['name'])
    artist_name = sp.currently_playing()['item']['artists'][0]['name']

    # RETRIEVES ALBUM NAME
    print(sp.currently_playing()['item']['album']['name'])
    album = sp.currently_playing()['item']['album']['name']

    output_str = tk.StringVar()

    output_str.set('Current Song:\n%s\n%s\n%s' % (song_name, artist_name, album))

    spotify_labels = tk.Label(widget, textvariable=output_str, bg='#00ff00', justify='left', font='Courier 44 bold', fg='white')

    widget.update_idletasks()
    widget.update()

    while True:
        progress = sp.currently_playing()['progress_ms']
        duration = sp.currently_playing()['item']['duration_ms'] - 900

        widget.configure(bg='#00ff00')

        #print(progress)
        #print(duration)

        if progress >= duration or progress < 900:

            spotify_labels.destroy()

            # RETRIEVES SONG NAME
            #print(sp.currently_playing()['item']['name'])
            song_name = sp.currently_playing()['item']['name']

            # RETRIEVES ARTIST NAME
            #print(sp.currently_playing()['item']['artists'][0]['name'])
            artist_name = sp.currently_playing()['item']['artists'][0]['name']

            # RETRIEVES ALBUM NAME
            #print(sp.currently_playing()['item']['album']['name'])
            album = sp.currently_playing()['item']['album']['name']

            output_str = tk.StringVar()

            output_str.set('Current Song:\n%s\n%s\n%s' % (song_name, artist_name, album))

            spotify_labels = tk.Label(widget, textvariable=output_str, bg='#00ff00', justify='left', font='Courier 44 bold', fg='white')
            spotify_labels.pack()

            widget.update_idletasks()
            widget.update()

else:
    print('Cannot Retrieve Token For ' + SPOTIFY_USERNAME)