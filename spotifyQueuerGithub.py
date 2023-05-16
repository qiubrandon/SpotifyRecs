import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace 'YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET', and 'YOUR_REDIRECT_URI' with your actual credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-read-recently-played,user-read-private,user-read-currently-playing,user-modify-playback-state')
access_token = sp_oauth.get_access_token(as_dict=False)
sp = spotipy.Spotify(auth=access_token)

current_track = sp.current_user_playing_track()
# for item in current_track["item"].keys():
#     print(item)

if current_track is not None:
    track_name = current_track['item']['name']
    artist_name = current_track['item']['artists'][0]['name']
    print("Currently playing:", track_name, "by", artist_name)
else:
    print("No track is currently playing.")
    exit()

while True:
    songNum = input("How many recommended songs do you want to queue? \n")
    try:
        songNum = int(songNum)
        break
    except ValueError:
        print("Please enter a valid amount!")


recommendations = sp.recommendations(seed_tracks=[current_track["item"]["uri"]], limit = songNum)
r = recommendations
# for item in r["tracks"]:
#     print(str(item) + "\n")

if (len(recommendations) > 0):
    print("Queued: \n")
    for j in range(songNum):    
        recSong = recommendations["tracks"][j]
        print(str(recSong["name"]) + " - " + str(recSong["album"]["artists"][0]["name"]) )
        sp.add_to_queue(recSong["uri"])
else:
    print("No recommendations.")