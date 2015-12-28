from class_weapons import Weapons
from class_player import Player

gun = Weapons("Gun", 10, 0)
p = Player("Vishesh", gun)
print p.name
print p.weapon.name