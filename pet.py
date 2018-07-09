
class Pet():

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def assign_owner(self, owner):
        self.owner = owner

    def __str__(self):
        return f'My name is {self.name}, I have {self.animal_type.leg_num} legs, and I say {self.animal_type.speak()}'