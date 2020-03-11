"""
Item should have a name and description
name should be one word
Base Class
"""


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.description}'

    def __repr__(self):
        return f'{self.name} - {self.description}'

    def on_take(self):
        print(f'You have picked up {self.name}.')

    def on_drop(self):
        print(f'You have dropped {self.name}.')


items = {
    "1_up_mushroom": Item('1-UP Mushroom', ''),
    "Anchor": Item('Anchor', ''),
    "Blue Coin": Item('Blue Coin', ''),
    "Card": Item('Card', ''),
    "Coin": Item('Coin', ''),
    "Fire Flower": Item('Fire Flower', ''),
    "Frog Suit": Item('Frog Suit', ''),
    "Goomba\'s Shoe": Item('Goomba\'s Shoe', ''),
    "Hammer": Item('Hammer', ''),
    "Hammer Suit": Item('Hammer Suit', ''),
    "Lakitu\'s Cloud": Item('Lakitu\'s Cloud', ''),
    "Magic Ball": Item('Magic Ball', ''),
    "Magic Wand": Item('Magic Wand', ''),
    "Music Box": Item('Music Box', ''),
    "P-Wing": Item('P-Wing', ''),
    "Recorder": Item('Recorder', ''),
    "Reverse Mushroom": Item('Reverse Mushroom', ''),
    "Super Leaf": Item('Super Leaf', ''),
    "Super Mushroom": Item('Super Mushroom', ''),
    "Super Star": Item('Super Star', ''),
    "Tanooki Suit": Item('Tanooki Suit', '')
}