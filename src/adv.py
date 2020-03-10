from src.player import Player
from src.room import Room

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
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

def pretty_print(fn):
    def wrapper(cur_room):
        middle_line = len(f'{cur_room}')
        if middle_line > 60:
            middle_line = 60
        top_line = ''
        for letter in range(middle_line):
            top_line = top_line + '*'

        print(top_line)
        print(f'{cur_room}')
        print(top_line)

    return wrapper


@pretty_print
def print_location(cur_room):
    pass


def moves(user, move):
    if move == 'n':
        return user.room.n_to
    elif move == 's':
        return user.room.s_to
    elif move == 'w':
        return user.room.w_to
    else:
        return user.room.e_to


def main():
    player_name = input('Please enter your name-> ')
    player = Player(player_name, room['outside'])
    print(f'Welcome {player_name} to the Dungeon Crawl')
    while True:
        # Print
        print_location(player.room)
        cmd = input('-> ')
        if cmd == 'q':
            print('Come back again, you hear!')
            break
        elif cmd == 'n' or cmd == 's' or cmd == 'w' or cmd == 'e':
            if moves(player, cmd) is None:
                print('You hit a wall, move not allowed, -50dkp')
                continue
            else:
                player.room = moves(player, cmd)
        else:
            print('Please enter a valid direction: n,s,w,e')
            continue


if __name__ == '__main__':
    main()
