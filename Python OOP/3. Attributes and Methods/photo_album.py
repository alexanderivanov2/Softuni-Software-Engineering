class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [] * pages
        self.row = 0
        self.col = 0

    @staticmethod
    def update_row_and_col(row, col):
        if col + 1 == 4:
            row += 1
            col = 0
        else:
            col += 1
        return row, col

    @staticmethod
    def check_next_free_slot(pages, row):
        return pages == row

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        if self.check_next_free_slot(self.pages, self.row):
            return "No more free slots"
        self.photos[self.row].append(label)
        page = self.row + 1
        slot = self.col + 1
        self.row, self.col = self.update_row_and_col(self.row, self.col)
        return f"{label} photo added successfully on page {page} slot {slot}"

    def display(self):
        line = '-' * 11
        result = ''
        for row in self.photos:
            result += f"{line}\n"
            result += f"{' '.join('[]' for el in row)}\n"

        result += line
        return result
