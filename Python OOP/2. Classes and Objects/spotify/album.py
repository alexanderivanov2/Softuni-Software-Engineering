from project.song import Song

class Album:
    def __init__(self, name, songs=[]):
        self.name = name
        self.songs = songs
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        for s in self.songs:
            if s.name == song_name:
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):

        songs = '\n'.join(f"== {s.get_info()}" for s in self.songs)
        return f"Album {self.name}\n{songs}"