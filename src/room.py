# Implement a class to hold room information. This should have name and
# description attributes.
from itemClass import Food, Egg

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    def __str__(self):
        return_string = "---------"
        return_string += "\n\n"
        return_string += self.name
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n\n"
        return_string += f"{self.get_exits_string()}"
        return_string += "\n\n"
        return_string += "Room has:\n\n"
        return_string += f"{self.print_items()}"
        return return_string
    def get_exits_string(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits
    
    def print_items(self):
        items= []
        for item in range(len(self.items)):
            items.append(self.items[item])
        return items
    