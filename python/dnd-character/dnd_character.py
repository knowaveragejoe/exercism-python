from random import randint, choice
from math import floor

class Character:
    def __init__(self):
        self.strength = self.get_stat()
        self.dexterity = self.get_stat()
        self.constitution = self.get_stat()
        self.intelligence = self.get_stat()
        self.wisdom = self.get_stat()
        self.charisma = self.get_stat()

        self.hitpoints = 10 + modifier(self.constitution)

    def get_stat(self):
        rolls = [randint(0, 6) for roll in range(0, 4)]
        rolls.sort()

        return sum(rolls[-3:])
    
    def ability(self):
        return getattr(self, choice(['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']), None)

def modifier(constitution):
    return floor((constitution - 10) / 2)