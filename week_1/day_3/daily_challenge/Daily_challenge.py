class Farm():
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    def get_info(self):
        print(self.name, "'s farm \n")
        for animal, count in self.animals.items():
            print (animal, ":", count )
        print( "\n   E-I-E-I-0!")    

farm = Farm("Sunny Farm")
farm.add_animal("cow", 5)
farm.add_animal("chicken", 10)
farm.add_animal("pig", 3)
farm.add_animal("cow", 7)
farm.get_info()
    
