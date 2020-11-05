from spotify_client import SpotifyClient


def main():
    artist_query = input('Enter an artist: \n')
    client = SpotifyClient()
    top_songs = client.get_artist_top_songs(artist_query, 5)

    print('Here is ' + artist_query + '\'s top 5 songs:')
    for index, track in enumerate(top_songs):
        print(index, track[0])


main()
