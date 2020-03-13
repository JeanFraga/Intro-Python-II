from room import Room
from player import Player
from itemClass import Item, Food, Egg

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

rock = Item("rock", "This is a rock.")
sandwich = Food("sandwich", "This is a delicious sandwich.", 100)
egg = Egg()

room['outside'].items.append(rock)
room['overlook'].items.append(sandwich)
room['treasure'].items.append(egg)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

name = input("Player name: ")
if name == "":
    name = "Jhon"
player = Player(name, room['outside'])
print(f"Hello {player.name}")
print(player.current_room)
action = None
valid_directions = ("n", "s", "e", "w")
while action != "q":
    # print(room['outside'].items[0])
    action = input("\n~~> ")
    if action == "q":
        print("\nThank you for playing! Come again :D\n")
    # if action == "q":
    #     print("Goodbye!")
    #     exit(0)
    elif action in valid_directions:
        player.travel(action)
    elif action == "i":
        player.print_inventory()
    elif "get" in action:
        action = action.split(" ")[1]
        if getattr(room.items, f"{action}"):
            player.items.append(getattr(room.items, f"{action}"))
            print(f"picked up {action}")
        else:
            print("Item does not exist in this room.")
    else:
        print("I did not understand that command")
