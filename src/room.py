# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player

class Room(Player):
    def __init__(self, name, room):
        super().__init__(name, room)
        # self.attributes = attributes
    def __str__(self):
        return f"{self.name}{self.room}"