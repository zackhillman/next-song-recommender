import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

data = []
users = ['spotify', 'patreeeek', 'christopherkozich', 'thebund_pablo', '121410021', 'aofd3', 'eardrumspop', 'esalaukkanen', '1217281510', '127785929', 'khdtx25', 'sonymusicentertainment', 'filtr', 'digster.fm', '1214110112', 'dkoy', 'digsterdeutschland', 'trabbey', 'yrkjs6dnap7oc1bjc33f95h1d', '1263240308', 'edmsauce', 'iampetey', 'playstation_music', 'fzzbfl1cna7ksjqn4x73egnad', 'l70mtbcfoapp3mst5n81hlkz9', '1245722571', 'warnermusicus', 'yrkjs6dnap7oc1bjc33f95h1d', 'filtr.br', 'filtr.au']
for user in users:
    playlists = sp.user_playlists(user)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            songs = sp.user_playlist_tracks(user, playlist['id'])
            while songs:
                for song in songs['items']:
                    data.append(pd.DataFrame([[user, playlist['name'], song['track']['name'], song['track']['artists'][0]['name']]], columns= ['user_id', 'playlist_name', 'track', 'artist']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

df = pd.concat(data, ignore_index=True)
df.to_csv('datasets/spotify/spotify_scraped_dataset.csv')
