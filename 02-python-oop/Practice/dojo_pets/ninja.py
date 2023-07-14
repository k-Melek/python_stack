from pet import Pet

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

        


max = Pet("Max", "Dog", ["Sit", "Roll Over"])
melek = Ninja("Melek", "Khedher", "Biscuits", "Dog Food", max)

melek.feed()
melek.bathe()
melek.walk()