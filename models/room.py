class Room:
    def __init__(self, room_num:int, available_beds:int=8, taken_beds:int=0):
        self.room_num = room_num
        self.available_beds = available_beds
        self.taken_beds = taken_beds


    def assign_bed(self):
        if self.available_beds > self.taken_beds:
            self.taken_beds += 1
            self.available_beds -= 1
        else:
            print("Sorry, there are no available beds in this room")