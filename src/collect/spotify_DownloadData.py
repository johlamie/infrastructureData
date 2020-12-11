# Installer le package ci-dessous avant
#!pip install spotipy

import spotipy
import json

#définition des variables utilisateur:
CLIENT_ID="7a37fb7eb8a7444294491f8dd4488c83"
CLIENT_SECRET="d75fb92060b6440b8f29f26f00c0310a"

#Connection:
from spotipy.oauth2 import SpotifyClientCredentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

#test de récuperer les 20 premières chansons:
def getArtistTrack(name, limit):
    results = sp.search(q=name, limit=limit)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])

#Get Artist Struct
def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

#Afficher les albums d'un artiste
def show_artist_albums(artist):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    seen = set()  # to avoid dups
    albums.sort(key=lambda album: album['name'].lower())
    for album in albums:
        name = album['name']
        if name not in seen:
            print('ALBUM: %s', name)
            seen.add(name)

# Get new released:
# TODO : Idéalement il faut retourné un objet
def getNewReleased():
    response = sp.new_releases()
    while response:
        albums = response['albums']
        for i, item in enumerate(albums['items']):
            print(albums['offset'] + i, item['name'])

        if albums['next']:
            response = sp.next(albums)
        else:
            response = None



# Appel aux méthodes ici
if __name__ == '__main__':
    get_artist('Dehmo')
    show_artist_albums(get_artist('Dehmo'))
    getArtistTrack('Booba', 10)
    getNewReleased()