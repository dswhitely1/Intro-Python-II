# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def print_items(self):
        print('--- Current Inventory Items ---')
        for item in self.items:
            print(item)
        print('-------------------------------')

    def add_items(self, item):
        self.items.append(item)
