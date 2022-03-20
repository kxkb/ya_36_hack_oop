"""

"""
class Thing:

    def __init__(self, thing_name, thing_protection, thing_attack, thing_hp):
        self.thing_name = thing_name
        self.thing_protection = thing_protection
        self.thing_attack = thing_attack
        self.thing_hp = thing_hp
    

class Person:
     
    def __init__(self, name, hp, base_attack, base_protection):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_protection = base_protection


    def set_things(things):
        pass


    def minis_hp(main):
        pass

class Paladin(Person):

    def __init__ (self, name, hp, base_attack, base_protection):
        super().__init__(name, base_attack)
        self.hp = hp * 2
        self.base_protection = base_protection * 2

class Warrior(Person):

    def __init__ (self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_protection)
        self.base_attack = base_attack * 2
