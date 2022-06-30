class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.list_songs = Album.add_songs(self, songs)
        self.published = False

    def add_songs(self, songs):
        dict_songs = {}
        for song in songs:
            dict_songs[song.name] = song
        return dict_songs

    def add_song(self, current_song):
        if current_song.single:
            return f"Cannot add {current_song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif current_song.name in self.list_songs:
            return "Song is already in the album."
        self.list_songs[current_song.name] = current_song
        return f"Song {current_song.name} has been added to the album {self.name}."

    def remove_song(self, current_song):
        if self.published:
            return "Cannot remove songs. Album is published."
        if current_song not in self.list_songs:
            return "Song is not in the album."
        self.list_songs.pop(current_song)
        return f"Removed song {current_song} from album {self.name}."
        # for check_song in self.list_songs:
        #     if current_song == check_song.name:
        #         self.list_songs.remove(check_song)
        #         return f"Removed song {current_song} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        first = f"Album {self.name}\n"
        if self.list_songs:
            second = '\n'.join(f"== {el.get_info()}" for el in self.list_songs.values())
            return first + second + "\n"
        return first
