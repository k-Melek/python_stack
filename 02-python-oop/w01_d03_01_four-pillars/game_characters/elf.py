import character

#import 2 all character file

class Elf(character.Character):
    def __init__(self, name):
        super().__init__(name)
    def magic_attack(self, target):
        target.health -= self.power
        target.power -= 20
        target.defence -= 20
