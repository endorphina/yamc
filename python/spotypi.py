import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

####### CREDENITALS
# => https://developer.spotify.com/dashboard
CLIENT_ID='xxxxxxxxxxxxxx' # past your client_id, as given by spotify develpment dashboard
CLIENT_SECRET='xxxxxxxxxxxxxx' # past your client_secret, as given by spotify develpment dashboard
REDIRECT_URL='http://localhost/callback/' # past your callback url as set in spotify development dashboard

######## SCOPES
scope = "user-read-playback-state,user-modify-playback-state"

######## DEVICES
DEVICE = 'xxxxxxxxxxxxxxxxxxxx' # Spotify Device ID


######## PLAYLISTS & TRACKS
PLAYLIST_ID = "xxxxxxxxxxxxxx"




CONTEXT_CALL = "spotify:playlist:" + PLAYLIST_ID
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL, scope=scope, open_browser=False ))

######## VOLUME CONTROL
sp.volume(90, device_id=DEVICE)

# play given playlist
sp.start_playback(device_id=DEVICE, context_uri=CONTEXT_CALL)


# Next Titel
sp.next_track()
sleep(10)

# Previous Titel
sp.previous_track()
sleep(10)

# pause playback
sp.pause_playback()

