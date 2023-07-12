
class Ninja: 
    # * CLASS Attributes
    dojo = "Tokyo"
    all_ninjas = []

    #! Constructor 
    def __init__(self, name, age) :
        #* ATTRIBUTES
        self.name = name
        self.age = age
        #* ATTRIBUTES with default values
        self.health = 50
        self.power = 10
        Ninja.all_ninjas.append(self)

    #! METHODS 
    def attack(self, target):
        target.health-= self.power
        print (f"[ATTACK] {self.name} attacked {target.name} And caused Damage equal {self.power}")
        return self
    
    def heal(self):
        self.heal +=20
        return self
    
    # - STATIC METHOD 
    @staticmethod
    def validate_ninja (dict):
        is_valid = True
        if len(dict ['name'] ) < 2:
            is_valid = False
        if dict ['age'] < 17 :
            is_valid = False
        return is_valid
    
    # - CLASS METHOD 
    @classmethod
    def boot_camp(cls):
        for ninja in cls.all_ninjas:
            ninja.health +=20
            ninja.power +=10
        return cls

#Create an instance (object) of the class NINJA
john = Ninja("John", 41)
alex = Ninja("Alex", 23)
print("before : ",alex.health)
john.attack(alex)
print("after : ",alex.health)
print(john.name, john.health) 
