class ArmyBase:
    def __init__(self,name:str):
        self.name = name
        self.houses = []
        self.full_houses = []

    def add_house(self, house:"House"):
        self.houses.append(house)

    def update_houses(self):
        for house in self.houses:
            if house.house_full():
                self.full_houses.append(house)



