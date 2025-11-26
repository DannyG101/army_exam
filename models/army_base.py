class ArmyBase:
    def __init__(self,name:str, houses:list["House"]):
        self.name = name
        self.houses = houses

    def add_room(self, house:"House"):
        self.houses.append(house)