from spotify_client import SpotifyClient
import datetime


def main():
    artist_query = input('Enter an artist: \n')
    client = SpotifyClient()
    top_songs = client.get_artist_top_songs(artist_query, 5)
    print('Here is ' + artist_query + '\'s top 5 songs:')
    for index, track in enumerate(top_songs):
        print(index+1, track['name'])

    latest_song = client.get_artist_latest_song(artist_query)
    print('\nHere is there latest song:')
    print(latest_song['name'] + ' released on ' +
          str(latest_song['release_date'].ctime()))


main()
