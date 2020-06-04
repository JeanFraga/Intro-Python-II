class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return self.name

class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories
    def __str__(self):
        return self.name
class Egg(Food):
    def __init__(self):
        super().__init__("egg", "This is an egg", 20)
    def __str__(self):
        return self.name