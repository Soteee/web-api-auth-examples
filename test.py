from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import pprint

pp = pprint.PrettyPrinter(indent=1)

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = 'https://open.spotify.com/playlist/3H7JIDBJYpsT6SWlodnljO?si=e6187b130b9c42ed'
results = sp.playlist(playlist_id)

for r in results['tracks']['items']:
    pp.pprint(type(r))