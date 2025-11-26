from models.soldier import Soldier

def list_to_soldier_object(line:list):
    personal_id_list = list(line[0])
    if personal_id_list[0] != "8":
        return None
    else:
        try:
            personal_id = int(line[0])
            first_name = line[1]
            last_name = line[2]
            gender = line[3]
            city = line[4]
            distance_from_base = int(line[5])

        except ValueError as err:
            return f"There is a error in one of the fields of this object : {err}"

        else:
            print("Nothing went wrong")
            return Soldier(personal_id, first_name, last_name, gender, city, distance_from_base)

def assign_rooms(soldiers_list, army_base):
    for soldier in soldiers_list:
        if len(army_base.full_houses) < len(army_base.houses):
            for house in army_base.houses:
                if len(house.full_rooms) < len(house.rooms):
                    for room in house.rooms:
                        if room.taken_beds < 8:
                            room.assign_bed_to_soldier(soldier)
                            soldier.has_a_place = True
                            soldier.location = f"{soldier.first_name} is staying in {house.name}, in room number {room.room_num}"


