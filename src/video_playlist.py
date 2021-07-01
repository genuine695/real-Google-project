"""A video playlist class."""
from .video_library import VideoLibrary


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self):
        self._playlists={}
        for x in self._playlists:
            print("needs to be completed")

    def get_all_playlist(self):
        """Returns all available playlists."""
        return list(self._playlist.values())

    def get_playlist(self, playlist_name):
        """Returns playlists as objects."""
        return self._playlist.get(playlist_name, None)






