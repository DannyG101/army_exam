


class House:
    def __init__(self,name:str):
        self.name = name
        self.rooms = []
        self.full_rooms = []

    def add_room(self, room:"Room"):
        self.rooms.append(room)

    def update_rooms(self):
        for room in self.rooms:
            if room.room_is_not_available():
                self.full_rooms.append(room)
    def house_full(self):
        if len(self.full_rooms) == len(self.rooms):
            return True
        return False

