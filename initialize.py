from random import randint
from class_weapons import Weapons
from class_weapons import Guns
from class_weapons import Grenade
from class_player import Player
from class_dragon import Dragon

Commands = {
    'quit' : Player.exitgame,
    'help' : Player.askhelp,
    'status' : Player.status,
    'attack' : Player.attack,
    'throwgrenade': Player.throwgrenade,
}

gun = Guns("Gun", 10, -1)
grenade = Grenade("Grenade", 50, 25)
player = Player("Player", gun, grenade, Commands)
dragon = Dragon(1, 100,100, 5)


