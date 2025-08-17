#exerrcise 1


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    pass


sara_bengal = Bengal("Sara's Bengal", 2)
sara_chartreux = Chartreux("Sara's Chartreux", 3)
sara_siamese = Siamese("Sara's Siamese", 4)

all_cats = [ sara_bengal, sara_chartreux, sara_chartreux ] 
sara_pets = Pets(all_cats)
sara_pets.walk()




#exerrcise 2

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        speed = self.weight / self.age * 10
        return speed 
    
    def fight(self, other_dog):    
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            return f'{self.name} wins the fight against {other_dog.name}!'
        elif self.run_speed()*self.weight < other_dog.run_speed()*other_dog.weight:
            return f'{other_dog.name} wins the fight against {self.name}!'
        else:
            return f'{self.name} and {other_dog.name} are equally matched!'

dog_1= Dog("Buddy", 5, 20)
dog_2 = Dog("Max", 3, 25)   
dog_3 = Dog("Charlie", 4, 22)

print(dog_1.bark())
print(dog_2.name, "'s speed is :", dog_2.run_speed())
print(dog_3.fight(dog_1))



#exercise 3 (go to week_1/day_4/exercices/exercise_3.py)

#exercice 4

class Family():
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, **kwargs):
        self.members.append(kwargs)
        print ("Congratulation on the new family member!")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
             return member["age"] >= 18
        return print(f"{name} is not in the family.")
    
    def family_presentation(self):
        print(f"The {self.last_name} family has the following members:")
        for member in self.members:
            print(f"{member['name']}, {member['age']} years old, {member["gender"]}.")

bitahi = Family("BITAHI")
bitahi.born(name="Hicham", age = 55 , gender="Male", is_child=False)
bitahi.born(name="Zayad", age = 23 ,  gender="Male", is_child=False)

print("The father is an adult:", bitahi.is_18("Hicham"))

bitahi.family_presentation()

#exercice 5

class SuperPowerStuffMissing(Exception):
    pass

class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    return print(name,"'s power is :", member["power"])
                else:
                    raise Exception("The family member is not allowed to use their powers!")
        return  print(f"{name} is not in the family.")

    def born(self, **kwargs):
        if  "power" not in kwargs or "incredible_name" not in kwargs:
            raise SuperPowerStuffMissing("Incredible family members must have a power and a superhero name.")
        super().born(**kwargs)

    def incredible_presentation(self):
        print("This is the", self.last_name, "super family!")
        super().family_presentation()
        for member in self.members:
           print(member['name'],"'s power is :", member['power'], "! And they are called", member['incredible_name'], "!")

incredibles = TheIncredibles("Incredibles")
incredibles.born(name = "Michael", age = 35, gender = "Male", is_child = False, power = "fly", incredible_name = "MikeyFlyer")
incredibles.born(name = "Sarah", age = 32, gender = "Female", is_child = False, power = "read minds", incredible_name = "Professor S")
incredibles.born(name = "Baby Jack", age = 1, gender = "Male", is_child = True, power = "Unknown", incredible_name = "CHAOS")

incredibles.incredible_presentation()