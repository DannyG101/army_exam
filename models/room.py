class Room:
    def __init__(self, room_num:int):
        self.room_num = room_num
        self.soldiers = []
        self.available_beds = 8
        self.taken_beds = 0


    def assign_bed_to_soldier(self, soldier:"Soldier"):
        if self.available_beds > self.taken_beds:
            self.soldiers.append(soldier)
            self.taken_beds += 1
        else:
            print("Sorry, there are no available beds in this room")

    def room_is_not_available(self):
        if self.taken_beds >= self.available_beds:
            return True
        return False