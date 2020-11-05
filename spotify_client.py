import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os


class SpotifyClient:
    def __init__(self):
        pass

    @classmethod
    def execute_query(cls, query, query_type, limit):

        scope = "user-library-read"
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                                                   client_secret=os.environ['SPOTIPY_CLIENT_SECRET']))
        results = sp.search(q=query, limit=limit, type=query_type)
        return results

    def get_top_artist(self, artist_query):

        # From the results find the top artist based on the popularity rating.
        artists_results = self.execute_query(artist_query, 'artist', 5)
        top_result = None
        for idx, artist in enumerate(artists_results['artists']['items']):
            if top_result is None:
                top_result = artist
            else:
                top_result_popularity = top_result['popularity']
                artist_popularity = artist['popularity']
                if artist_popularity > top_result_popularity:
                    top_result = artist

        return top_result

    def get_artist_top_songs(self, artist_query, limit):

        artist = self.get_top_artist(artist_query)
        # Fetch the artists tracks.
        tracks_details_full = self.execute_query(
            artist['name'], 'track', 50)

        tracks_details_canonical = []
        for index, track in enumerate(tracks_details_full['tracks']['items']):
            # Retrieve only the name and popularity rating from each track.
            tracks_details_canonical.append(
                [track['name'], track['popularity']])

        # Sort the tracks by popularity
        tracks_details_canonical.sort(key=lambda t: t[1], reverse=True)
        top_songs = tracks_details_canonical[:limit]

        return top_songs
