import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages

        self.photos = [[] for i in range(pages)]
        self.can_contain = 4
        self.row = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.ceil(photos_count / 4))

    def add_photo(self, label):
        if self.row == self.pages:
            return "No more free slots"
        self.photos[self.row].append(label)
        slot = len(self.photos[self.row])
        page = self.row + 1
        if len(self.photos[self.row]) == 4:
            self.row += 1
        return f"{label} photo added successfully on page {page} slot {slot}"

    def display(self):
        top = "-" * 11
        result = []
        result.append(top)
        for el in self.photos:
            length = len(el)
            line = ' '.join("[]" for i in range(length))
            line += "\n" + "-" * 11
            result.append(line)
        return "\n".join(result)


album = PhotoAlbum(2)
print(album.display())
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))

print(album.display())
