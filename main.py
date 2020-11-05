from spotify_client import SpotifyClient


def main():
    artist_query = input('Enter an artist: \n')
    client = SpotifyClient()
    client.get_artist_details(artist_query)


main()
