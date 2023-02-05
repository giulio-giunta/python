playlist = {}
songs = []

for i in range(0,10):
	songs.append('song'+str(i))

properties = ['title', 'artist', 'album', 'date_added', 'duration']
properties = dict().fromkeys(properties, 'unknown')

songs = dict().fromkeys(songs, properties)
print(songs)

playlist.update(songs)
playlist.update({'name': 'my_playlist', 'author': 'giulio'})
print(playlist)