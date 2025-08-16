from exercises import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight,)
        self.trained = trained
    
    def train(self):
        self.trained = True
        print(self.bark())

    def play(self, *args):
       dog_names = [dog.name for dog in args]
       print(" and ".join(dog_names + [self.name]), "are playing together!")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll!",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))
            

