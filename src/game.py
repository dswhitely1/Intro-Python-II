from src.utils import pretty_print


class Game:
    def __init__(self, rooms, player):
        self.rooms = rooms
        self.player = player

    def __str__(self):
        print(f'Welcome {self.player.name} to the Super Mario Dungeon Crawl')

    @pretty_print
    def print_location(self):
        print(f'{self.player.current_room}')
        self.player.current_room.print_items()

    def moves(self, move):
        if move == 'n':
            return self.player.current_room.n_to
        elif move == 's':
            return self.player.current_room.s_to
        elif move == 'w':
            return self.player.current_room.w_to
        else:
            return self.player.current_room.e_to

    def direction_input(self, cmd):
        if cmd == 'q':
            print('Come back again, you hear!')
            exit(0)
        elif cmd == 'i' or cmd == 'inventory':
            self.player.print_items()
        elif cmd == 'n' or cmd == 's' or cmd == 'w' or cmd == 'e':
            if self.moves(cmd) is None:
                print('You hit a wall, move not allowed, -50dkp')
            else:
                self.player.current_room = self.moves(cmd)
        else:
            print('Please enter a valid direction: n,s,w,e')

    def action_input(self, verb, items):
        item = ''
        for word in items:
            item = item + f'{word} '
        item = item[:-1]
        if verb not in ['get', 'take', 'drop']:
            print(f'Invalid command: {verb}')
        elif verb.lower() == 'get' or verb.lower() == 'take':
            if len(self.player.current_room.items) > 0:
                found_item = False
                for each_item in self.player.current_room.items:
                    if each_item.name.lower() == item.lower():
                        each_item.on_take()
                        found_item = True
                        self.player.items.append(each_item)
                        self.player.current_room.items.remove(each_item)
                if not found_item:
                    print('Item is not in the room')
            else:
                print(f'No Items found in room')
        else:
            found_item = False
            for each_item in self.player.items:
                if each_item.name.lower() == item.lower():
                    each_item.on_drop()
                    self.player.items.remove(each_item)
                    self.player.current_room.items.append(each_item)
                    found_item = True
            if not found_item:
                print('Item is not in your inventory')

    def user_input(self):
        cmd = input(f'{self.player.name} -> ')
        if len(cmd.split(' ')) == 1:
            self.direction_input(cmd)
        else:
            verb = cmd.split(' ')[0]
            items = cmd.split(' ')[1:]
            self.action_input(verb, items)

    def main(self):
        while True:
            self.print_location()
            self.user_input()
