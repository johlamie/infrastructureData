# Installer le package ci-dessous avant
#!pip install spotipy

import spotipy
import json
import pandas as pd

from spotipy.oauth2 import SpotifyClientCredentials
from datetime import date




#définition des variables utilisateur:
CLIENT_ID="7a37fb7eb8a7444294491f8dd4488c83"
CLIENT_SECRET="d75fb92060b6440b8f29f26f00c0310a"

#Connection:
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

artist_name = []
track_name = []
popularity = []
track_id = []
release_date = []

for i in range(0, 2000, 50):
    track_results = sp.search(q='year:2020', type='track', limit=50, offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
        release_date.append(t['album']['release_date'])

df_tracks = pd.DataFrame({'artist_name':artist_name,'track_name':track_name,'track_id':track_id,'popularity':popularity,'date':release_date})
df_tracks.drop_duplicates()
track_results = sp.search(q='year:2020')

# Export des données dans des fichiers JSON
today = date.today().strftime("%Y-%m-%d")
file = 'data/{}.json'.format(today)
with open(file, "w") as f:
    json.dump(track_results, f, sort_keys=True)
    f.write('\n')
f.close()