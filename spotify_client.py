import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os


class SpotifyClient:
    def __init__(self):
        pass

    def get_artist_details(self, query):

        def execute_query(self, query, queryType, limit):

            scope = "user-library-read"
            sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                                                       client_secret=os.environ['SPOTIPY_CLIENT_SECRET']))
            results = sp.search(q=query, limit=limit, type=queryType)

            return results

        # From the results find the top artist based on popularity.
        artists_results = execute_query(self, query, 'artist', 5)
        top_result = None
        for idx, artist in enumerate(artists_results['artists']['items']):
            if top_result is None:
                top_result = artist
            else:
                top_result_popularity = top_result['popularity']
                artist_popularity = artist['popularity']
                if artist_popularity > top_result_popularity:
                    top_result = artist

        # Fetch the artists tracks.
        artist_tracks = execute_query(self, top_result['name'], 'track', 50)
        for idx, track in enumerate(artist_tracks['tracks']['items']):
            print(idx, track['name'], track['popularity'], )
