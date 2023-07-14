
class Pet:
    def __init__(self ,name , type , tricks) :
        self.name = name
        self.pet_type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
    
    def sleep(self):
        self.energy+=25
        print(f"{self.name} slept and gained 25 energy")

    def eat(self, food):  
        self.energy += 5
        self.health += 10
        print(f"{self.name} ate {food} and gained 5 energy and 10 health.")

    def play(self):
        self.health += 5
        print(f"{self.name} played and gained 5 health.")

    def noise(self):
        if self.pet_type == "Dog":
            print(f"{self.name} says: Woof!")
        elif self.pet_type == "Cat":
            print(f"{self.name} says: Meow!")
        else:
            print(f"{self.name} made a noise.")


class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Dog", tricks)

    def bark(self):
        print(f"{self.name} : Woof!!!")

    def roll(self):
        print(f"{self.name} Rolls on its BACK!")