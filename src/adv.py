from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance\n",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer\n", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook\n", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage\n", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber\n", """You've found the long-lost treasure
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

def checklegal(action):
    # if 
        return False

name = input("Player name: ")
if name == "":
    name = "Jhon"
player = Player(name, room['outside'])
print(player)
action = None
while action != "q":
    exitgame = {"q":"q"}
    choices = { "n":"n_to", "s":"s_to", "e":"e_to", "w":"w_to", "q":"q"}
    action = input("You can try to move North(n), South(s), East(e), West(w). Type (q) to Quit. Enter choice: ")

    if action in choices:
        # print(choices[action])
        player = Player(name, room["outside"].n_to)

        print(player)

    if action not in (choices or exitgame):
        print("Entered wrong choice. \n")

    if action == "q":
        print("\nThank you for playing! Come again :D\n")
