# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name="Jhon", room="outside"):
        self.name = name
        self.room = room
    def __str__(self):
        return f"{self.name} is in room {self.room}"