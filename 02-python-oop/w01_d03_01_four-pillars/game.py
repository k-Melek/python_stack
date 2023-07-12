class Character :
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.power = 50
        self.defence = 30
        self.weapon = None
    
    def attack (self, target):
        target.health-= self.power
        print (f"[ATTACK] {self.name} attacked {target.name}")
        damage = target.defend(self.power)  #! Abstraction method within method 
        print (f"And caused Damage equal {damage}")
        target.health -= damage
        return self
    
    def defend (self, damage):
        
        print (f"[DEFEND] {self.name} defended {damage} And reduced it by {self.defence}")
        damage -= self.defence
        return self

class Barbarian(Character): #! INHERITANCE CLASS 
    def __init__(self, name):
        super().__init__(name)
        self.power+= 30 # Polymorphism Change parent attribute
        self.health+= 20 # Polymorphism Change parent attribute
        self.rage = 30 # Polymorphism NEW Attribute

class Elf(Character):
    def __init__(self, name):
        super().__init__(name)
    def magic_attack(self, target):
        target.health -= self.power
        target.power -= 20
        target.defence -= 20

class Seer:
    def __init__(self):
        self.hidden_type = Barbarian("SEER1")
        

john = Character("JOHN")
conan = Barbarian("CONAN")
elon = Seer()
elon.hidden_type.attack(john)
print(f"Conan health: {conan.health}")

conan.attack(john)

jane = Character("JANE")