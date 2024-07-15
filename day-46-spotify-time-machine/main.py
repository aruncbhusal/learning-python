# For today, there was only a single video in the file, and there are hint steps but
# I don't think they're as helpful as I'd like them to be, but I'll follow it and 
# add required steps myself
# The project for today is Spotify Musical Time Machine, where we extract the top 100
# songs of a particular date and create a new playlist with those songs on Spotify so
# that we can feel the nostalgia from that point in time.

# For the date, I will need to use the datetime module
# import datetime
# For the web scraping part, I'll need requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup
# Now for the spotify part
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_USER_ID = "<USER_ID>"
SPOTIFY_CLIENT_ID = "<CLIENT_ID>"
SPOTIFY_CLIENT_SECRET = "<CLIENT_SECRET>"

# Now the first thing to do is to get a date input from the user
# I thought we'd need to use datetime but I probably won't. When I visited the Billboards
# website, it always went to the link for the Saturday of the week for the day I selected
# but looks like it works the same no matter what date you give in the URL for that week
# One less headache to deal with then

date = input("I'm here to take you to the past. Enter a date in YYYY-MM-DD format: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

all_songs = []
all_artists = []
for a in soup.find_all("ul", class_="o-chart-results-list-row"):
    all_songs.append(a.h3.getText(strip = True))
    all_artists.append(a.h3.find_next("span").getText(strip = True))
# For artists, let me see if a selector of "li ul li span" will do the trick, since the
# name of the class is incomprehensibly difficult
                # all_artists = soup.select(selector= "li ul li span")
# The way I used to get to the specific element didn't work, so I found a better way.
# Since there were multiple elements with similar tags/selectors, I had to get the
# entire row, and get its first h3 and the span right after h3 like what I did
# The code is from StackOverflow, though I didn't copy it entirely, it's the same.

# print(all_songs)
# print(all_artists)

# Now that we got the songs, it's time to get the spotify API to do its job
# First I had to create an app with https://developer.spotify.com/dashboard/create
# Since Authentication with Spotify is complicated because of its OAuth implementation
# For this case, we'll be using a python module called "Spotipy"
# I will need to install and import it first to use it 
# It claims to be a "lightweight API for Spotify WebAPI" which is what we're using
# The docs are at: https://spotipy.readthedocs.io/en/2.24.0/ which we'll follow

# Let's first setup the spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = SPOTIFY_CLIENT_ID,
                                                client_secret= SPOTIFY_CLIENT_SECRET,
                                                redirect_uri= "https://open.spotify.com",
                                                scope= "playlist-modify-private"
                                                ))
# The redirect uri is what I have used while setting up the app, the course has example.com
# From spotipy docs, the redirect uri can be any valid web address, doesn't need to be accessible
# Even https://localhost will work. But since I have set this already, let's just go with it.
# A URI is an identifier while a URL is a html link

# Now I don't know how to confirm whether I have authentication, since it doesn't pop up
# I'll just try to use it regardless, yes that was it, I just had to use it for it to prompt
# Next step is to search for the track on spotify, maybe giving the year and the track name
# Since a song might not be available on spotify, I'll have to add exception handling

# To create a playlist, we need to find out about the user first, the username is needed
                # print(sp.current_user())

# Before adding the songs to the playlist, we need to first create the playlist, so let's
# do that first, also using spotipy
pid = sp.user_playlist_create(user= SPOTIFY_USER_ID,
                        name= f"{date} Billboard 100",
                        public= False,
                        collaborative= False,
                        description="Test stuff")
song_uris = []

for song_name in all_songs:
    query = f"track:{song_name} year:{date.split('-')[0]}"
    # # I wonder if I can format it some other way, but this is what I got for now, replacing the
    # # space with a %20
    # response = requests.get(f"https://api.spotify.com/v1/search/{query}")
    # response.raise_for_status()
    # I was supposed to use Spotipy and not Spotify's get request, my bad
    try:
        track = sp.search(q= query, limit=1, type="track", market="US")
    except:
        pass
    else:
        song_uris.append(track["tracks"]["items"][0]["uri"])


sp.playlist_add_items(playlist_id= pid["id"],
                      items= song_uris)
print("Done!")