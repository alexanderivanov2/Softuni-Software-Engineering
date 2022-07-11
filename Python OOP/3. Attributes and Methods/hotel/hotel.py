class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        hotel_name = f"{stars_count} stars Hotel"
        print(hotel_name)
        return cls(hotel_name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number and room.capacity >= people and not room.is_taken:
                self.guests += people
                room.take_room(people)
                break
            elif room.number == room_number:
                room.take_room(people)
                break

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number and room.is_taken:
                self.guests -= room.guests
            room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms:" \
               f" {', '.join(str(room.number) for room in self.rooms if not room.is_taken)}\n" \
               f"Taken rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken)}"
