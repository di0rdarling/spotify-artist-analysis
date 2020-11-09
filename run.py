from spotify_client import SpotifyClient
import datetime


def main():
    artist_query = input('Enter an artist: \n')
    client = SpotifyClient()
    top_artist = client.get_top_artist(artist_query)
    if top_artist is not None:
        top_songs = client.get_artist_top_songs(top_artist['name'])
        print('Here is ' + artist_query + '\'s top ' +
              str(len(top_songs)) + ' songs:')
        for index, track in enumerate(top_songs):
            print(index+1, track['name'])

        latest_song = client.get_artist_latest_song(top_artist['name'])
        print('\nHere is their latest song:')
        print(latest_song['name'] + ' released on ' +
              str(latest_song['release_date'].ctime()))

        print('\nHere are their related genres:')
        artists_genres = client.get_artist_genres(top_artist['name'])
        for genre in artists_genres:
            print(genre)
    else:
        print('No results were found. Please enter another artist or a more valid search query.')


main()
