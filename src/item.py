"""
Item should have a name and description
name should be one word
Base Class
"""

import textwrap


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        wrapper = textwrap.TextWrapper(width=60)
        value = f'{self.name} - {self.description}'
        return wrapper.fill(text=value)

    def __repr__(self):
        return f'{self.name} - {self.description}'

    def on_take(self):
        print(f'You have picked up {self.name}.')

    def on_drop(self):
        print(f'You have dropped {self.name}.')


items = {
    "1_up_mushroom": Item('1-UP Mushroom', '1-Up Mushrooms are green mushrooms that give the player an extra life.'),
    "Anchor": Item('Anchor',
                   'The item is rare and can only be received at a special White Mushroom House after collecting a '
                   'certain number of coins in a certain level in the even-numbered worlds. An Anchor will prevent an '
                   'Airship from moving if Mario fails to clear it, thereby eliminating the need to trek long '
                   'distances to try again to complete the level. It also appears in cutscenes before Airship levels, '
                   'where Mario climbs the chain while the Anchor is being hoisted up.'),
    "Blue Coin": Item('Blue Coin',
                      'A special type of coin that first appeared in Super Mario Bros. 3 and have since appeared in '
                      'many later games.'),
    "Card": Item('Card',
                 'Cards are collectibles found at the goal in Super Mario Bros. 3. The player acquires one out of a '
                 'roulette every time a course is cleared; the pictures depicted are Mushrooms, Flowers and Stars. '
                 'Once three are collected, the player is given a 1-Up prize: one if they do not match, '
                 'two if Mushrooms, three if Flowers, and five if Stars.'),
    "Coin": Item('Coin', 'Coins (sometimes known as 1 Gold Coins[1] or Yellow Coins,[2] also called Mushroom coins in '
                         'the Beanbean Kingdom) are the main currency of the Mushroom Kingdom. They can be collected '
                         'in most Mario games. They have varying effects depending on the game type: In platformer '
                         'games, they increase a player\'s score and grant extra lives; in racing games, '
                         'they increase speed and recovery times; and in RPGs, they can be used to purchase items, '
                         'all among other uses.'),
    "Fire Flower": Item('Fire Flower', 'Fire Flowers are a power-up that are obtainable in many games in the Mario '
                                       'franchise, originating from Super Mario Bros. '),
    "Frog Suit": Item('Frog Suit', 'The Frog Suit is a power-up that debuted in Super Mario Bros. 3. The Frog Suit '
                                   'transforms Mario or Luigi into Frog Mario or Frog Luigi. It grants Mario or Luigi '
                                   'the power to jump higher, swim faster, and resist water currents better, '
                                   'but they can only hop while on land. When Frog Mario or Frog Luigi is hit by an '
                                   'enemy, they revert back to Super Mario or Super Luigi.'),
    "Goomba\'s Shoe": Item('Goomba\'s Shoe', 'A Goomba\'s Shoe, also known as the Shoe, is a large, green-colored '
                                             'boot with a wind-up key sticking out of the back of it. It is worn by a '
                                             'Shoe Goomba. It is one of the most uncommon of all the power-ups in all '
                                             'of the Mario franchise, and made its first game appearance in Super '
                                             'Mario Bros. 3, with the latest appearance in Super Mario Maker 2. The '
                                             'Goomba\'s Shoe was originally known in the PRG0 English NES release as '
                                             'Kuribo\'s Shoe, with "Kuribo" being the Japanese name of Goomba left '
                                             'unchanged.'),
    "Hammer": Item('Hammer', 'Hammers are items commonly used as weapons throughout the Mario franchise. They first '
                             'appear in Donkey Kong, in which they are used to smash barrels and enemies. Hammers are '
                             'usually thrown by the Hammer Bros and other enemies.'),
    "Hammer Suit": Item('Hammer Suit', 'The Hammer Suit[1][2] (alternatively Hammer Bros. Suit,[3][4] Hammer Brothers '
                                       'Suit,[5] or Hammer Brother Suit[6]) is an item found in Super Mario Bros. 3 '
                                       'and its remakes. This item transforms Mario or Luigi into Hammer Mario or '
                                       'Hammer Luigi, which gives them the ability to throw hammers.'),
    "Lakitu\'s Cloud": Item('Lakitu\'s Cloud', 'Lakitu\'s Clouds (originally Jugem\'s Cloud[1], "Jugem" being the '
                                               'romanization of Lakitu\'s Japanese name) are a type of cloud with a '
                                               'smiley face that Lakitus usually inhabit.'),
    "Magic Ball": Item('Magic Ball', 'Magic Balls first appear in Super Mario Bros. 3. They only appear in fortresses '
                                     'after the player defeats Boom Boom. Upon his defeat, Boom Boom will drop a '
                                     'Magic Ball, and Mario must touch it to destroy the fortress and therefore '
                                     'complete the level.'),
    "Magic Wand": Item('Magic Wand', 'The magic wands[1] are magic items that are often seen in the hands of the '
                                     'Koopalings & Magikoopas. In Super Mario Bros. 3, magic wands were stolen from '
                                     'the Mushroom World\'s kings, and were used to transform them into various '
                                     'helpless creatures (which varies between the NES version and the SNES/GBA '
                                     'remakes). '),
    "Music Box": Item('Music Box', 'The Music Box[1] is a common item found in Super Mario Bros. 3. It makes all '
                                   'Hammer Brother, Fire Brother, Boomerang Brother, and Sledge Brother Enemy '
                                   'Courses, as well as the Piranha Plant stages in Pipe Land, fall asleep so that '
                                   'Mario and Luigi can sneak past them.'),
    "P-Wing": Item('P-Wing', 'The P-Wing (originally Magic Wing[1]) is a special item that debuted in Super Mario '
                             'Bros. 3. The "P" stands for Paratroopa or Patapata (the Japanese name for that enemy). '
                             'It is considered a successor to the power-up simply known as the Wing.'),
    "Recorder": Item('Recorder', 'A Recorder[1][2], also known as a Magic Whistle[3][4] or Warp Whistle[5][6], '
                                 'is a rare item. It is originally from The Legend of Zelda; the six notes played '
                                 'upon use are identical, as is the whirlwind it summons that whisks the player to '
                                 'another location.'),
    "Reverse Mushroom": Item('Reverse Mushroom', 'A Reverse Mushroom is an uncommon type of Mushroom. It is the '
                                                 'opposite of a Super Mushroom, causing someone who is enlarged to '
                                                 'shrink and vice versa. This mushroom can be used against foes.'),
    "Super Leaf": Item('Super Leaf', 'A Super Leaf (also known as the Raccoon Leaf or Tanooki Leaf) is one of the '
                                     'many power-up items in the Mario franchise.  Super Leaves orginated in the game '
                                     'Super Mario Bros. 3, where they turn Mario or Luigi into Raccoon Mario or '
                                     'Raccoon Luigi, respectively.  As such, they grow raccoon ears and a raccoon '
                                     'tail, the latter of which lets them glide, fly after a running start, '
                                     'and tail whip.'),
    "Super Mushroom": Item('Super Mushroom', 'A Super Mushroom (also known as a Magic Mushroom,[1] a Power Booster '
                                             'Mushroom,[2] a Power-Up Mushroom,[3][4] or simply a Mushroom) is a red '
                                             'mushroom that serves a particular function depending on the game in '
                                             'which it is found. Its first and most common effect is causing Small '
                                             'Mario to turn into his Super form, allowing him to smash through bricks '
                                             'and take an extra hit from enemies.'),
    "Super Star": Item('Super Star', 'Super Stars (also parsed as Superstars,[1] alternatively referred to as '
                                     'Starmen, Invincible Stars,[2] or simply Stars[3][4]) are items used in many '
                                     'Mario games, including the Super Mario series and the Mario Kart series. If the '
                                     'player gets a Star, they will become invincible. '),
    "Tanooki Suit": Item('Tanooki Suit', 'The Tanooki Suit is a fairly uncommon item found in Super Mario Bros. 3 and '
                                         'its subsequent remakes. It is based on tanukis, Japanese creatures who, '
                                         'according to mythology, can use leaves to shape-shift and cause chaos. '
                                         'According to Shigeru Miyamoto in the Super Mario Bros. 3 entry of the 25th '
                                         'Anniversary Super Mario History Booklet, he was aware that most players '
                                         'outside Japan would be overall confused with the Tanooki Suit and the '
                                         'transformation, but he left it in anyways because it was cool and he was '
                                         'too excited to remove it.')
}
