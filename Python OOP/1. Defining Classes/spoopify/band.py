class Band:
    def __init__(self, name):
        self.name = name
        self.albums = {}

    def add_album(self, album):
        if album.name in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums[album.name] = album
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album):
        if album not in self.albums:
            return f"Album {album} is not found."
        if self.albums[album].published:
            return "Album has been published. It cannot be removed."
        self.albums.pop(album)
        return f"Album {album} has been removed."

    def details(self):
        first = f"Band {self.name}\n"
        if self.albums:
            second = '\n'.join(f"{el[1].details()}" for el in self.albums.items())
            return first + second + "\n"
        return first