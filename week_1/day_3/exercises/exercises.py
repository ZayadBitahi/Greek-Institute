#exercise 1:
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

first_cast = Cat("Morjana", 4)
second_cast = Cat("Loco", 1)
third_cast = Cat("Rimo", 6)

cats = [first_cast, second_cast, third_cast]

def oldest_cat(cats):
        if cats[0].age > cats[1].age and cats[0].age > cats[2].age:
            return cats[0]
        elif cats[1].age > cats[2].age:
            return cats[1]
        else:
            return cats[2]
        

oldest = oldest_cat(cats)
print("The oldest cat is", oldest.name , "and it is", oldest.age , "years old.")

#exercise 2:


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
         print(self.name , "goes woof!")
    
    def jump(self):
         jump_height = self.height * 2
         print(self.name , "jumps" , jump_height , "cm high!")
        
davis_dog = Dog("Rex", 50)
print(davis_dog.name,"is the name of Davis's dog, he is", davis_dog.height, "cm tall.")
davis_dog.bark()
davis_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name,"is the name of Sarah's dog, he is", sarahs_dog.height, "cm tall.")
sarahs_dog.bark()   
sarahs_dog.jump()

if davis_dog.height > sarahs_dog.height:
    print(davis_dog.name, "is taller than Sarah's dog.")
else:
    print( sarahs_dog.name,"is taller than Davis's dog.")



#exercise 3:

class Song:
     def __init__(self, lyrics):
         self.lyrics = lyrics
    
     def sing_me_a_song(self):
      for line in self.lyrics:
          print(line)

hello_adele = Song(["Hello from the other side", "I must have called a thousand times", "To tell you I'm sorry for everything that I've done"])
hello_adele.sing_me_a_song()

# exercise_4:


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name 
    
    def add_animal(self, new_animal):
        if new_animal in self.animals:
         print(new_animal, "is already in the zoo, please enter a different animal!")
        else:
            self.animals.append(new_animal)

    def get_animals(self):
        print("The animals in the zoo are:")
        for animal in self.animals:
            print(animal)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(animal_sold, "is not in the zoo, please enter a different animal!")

    def sort_animals(self):
        self.animals.sort()
        grouped = {}
        for animal in self.animals:
            if animal[0] not in grouped:
                grouped[animal[0]] = []
            grouped[animal[0]].append(animal)
        return grouped
    def get_groups(self):
        grouped = self.sort_animals()
        for letter,animal in grouped.items():
            print(letter , ":", animal)

new_york_zoo = Zoo("WildPark")

new_york_zoo.add_animal("lion")
new_york_zoo.add_animal("tiger")
new_york_zoo.add_animal("elephant")
new_york_zoo.add_animal("lemur")
new_york_zoo.add_animal("zebra")
new_york_zoo.add_animal("toucan")

new_york_zoo.get_animals()
new_york_zoo.sell_animal("zebra")
new_york_zoo.get_animals()
new_york_zoo.get_groups()




            
    
