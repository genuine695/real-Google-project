"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

# there is a problem with the IDE import
# if this happens please try and go tranverse outside of the src directory and enter py -m src.run into the terminal
    def __init__(self):
        self._current_vid = False
        self._current_paused = False
        self._video_library = VideoLibrary()




    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        vids = self._video_library.get_all_videos()
        vids.sort(key=lambda  x: x.title)

        for v in vids:
            name = str(v.tags)
            print(v.title, "(", v.video_id, ")", "[", name.strip("()"), "]")


        """Returns all videos."""


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global videos

        vid = self._video_library.get_video(video_id)
        videos = self._video_library.get_video(video_id)
        if self._current_vid is True:
            print("stopping video:", vid.title)
            self._current_vid = self._video_library.get_video(video_id)
            print("playing video:", vid.title)
            self._current_vid = True
        elif self._current_vid is False:
            print("playing video:", vid.title)
            self._current_vid = True
        else:
            print("video does not exist")



    def stop_video(self):
        """Stops the current video."""
        if self._current_vid is False:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:", videos.title)
            self._current_vid = False




    def play_random_video(self):
        """Plays a random video from the video library."""

        video = random.choice(self._video_library.get_all_videos())
        self.play_video(video._video_id)

    def pause_video(self):
        """Pauses the current video."""

        if self._current_vid is False:
            print("Cannot pause video: No video is currently playing")
        elif self._current_vid is True and self._current_paused is True:
            print("video already paused")
        else:
            print("Pausing video:", videos.title)
            self._current_vid = True
            self._current_paused = True




    def continue_video(self):
        """Resumes playing the current video."""

        if self._current_vid is False:
            print("Cannot continue video: No video is currently playing")
        elif self._current_vid is True and self._current_paused is False:
            print("It's already playing")
        else:
            print("Continue playing:",videos.title)
            self._current_vid = True

    def show_playing(self):
        """Displays video currently playing."""

        if self._current_vid is False:
            print("Cannot pause video: No video is currently playing")
        else:
            print("Now playing:", videos.title)
            self._current_vid = True

    def create_playlist(self, playlist_name):
        if len(self._playlists) >= 0:
            print("create new playlist", playlist_name)
            self._playlists.update(playlist_name)
            if playlist_name == self._playlists.get(playlist_name):
                print("cannot create playlist: a playlist with the name already exists")
            else:
                print("create new playlist", playlist_name)
                self._playlists.update(playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        if playlist_name == self._playlists.get(playlist_name):
            if self._video_library.get_video(video_id).title:
                for value in self._playlists.values():
                    if value == self._video_library.get_video(video_id).title:
                        self._playlists.update(playlist_name, video_id)
                        print("Added video to" + playlist_name + ":" + self._video_library.get_video(video_id).title)
                        break
                    else:
                        print("video already exists in the playlist")
            else:
                print("video does not exist")
        else:
            print("playlist already exists")

    def show_all_playlist(self):
        for x in self._playlists:
            print(x)

    def show_playlist(self, playlist_name):
        if playlist_name in self._playlists:
            print("playlist exists:", playlist_name)
        else:
            print("playlist does not exist")


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")






    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        vid = self._video_library.get_video(search_term)
        if vid:
            print("Here are the results" + search_term)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        vid_tag = self._video_library.get_video(video_tag)
        if vid_tag:
            print("Here are the results" + video_tag)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
