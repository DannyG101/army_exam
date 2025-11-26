class House:
    def __init__(self,name:str, rooms:list["Room"]):
        self.name = name
        self.rooms = rooms

    def add_room(self, room:"Room"):
        self.rooms.append(room)

