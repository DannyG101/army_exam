class Soldier:
    def __init__(self, personal_id:int, first_name:str, last_name:str, gender:str, city:str, distance_from_base:int, has_a_place:bool=False):
        self.personal_id = personal_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.distance_from_base = distance_from_base
        self.has_a_place = has_a_place
        self.location = "nowhere yet"