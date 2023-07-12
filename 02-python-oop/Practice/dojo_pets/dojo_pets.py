class Ninja:
    def __init__(self,first_name , last_name , treats , pet_food , pet) :
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self) :
        self.pet.play()
        print(f"{self.first_name} walked {self.pet.name}.")

    def feed(self) :
        self.pet.eat(self.pet_food)
        print(f"{self.first_name} fed {self.pet.name}.")

    def bathe(self):
        self.pet.noise()
        print(f"{self.first_name} bathed {self.pet.name}.")


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






max = Pet("Max", "Dog", ["Sit", "Roll Over"])
melek = Ninja("Melek", "Khedher", "Biscuits", "Dog Food", max)

melek.feed()
melek.bathe()
melek.walk()