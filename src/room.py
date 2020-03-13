# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.n_to = None
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f'{self.name} - {self.description}'

    def __repr__(self):
        return f'{self.name} - {self.description}'

    def print_items(self):
        print('--- Current Items in Room ---')
        for item in self.items:
            print(item)

    def add_items_to_room(self, item):
        self.items.append(item)
