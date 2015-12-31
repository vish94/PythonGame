from random import randint
from class_weapons import Weapons
from class_weapons import Guns
from class_weapons import Grenade
from class_player import Player
from class_dragon import Dragon

Commands = {
    'quit' : "Exit Game",
    'help' : "See all valid keywords",
    'status' : "Check player status",
    'attack' : "Attack dragon with the current Gun",
    'throwgrenade': "Throw granade on dragon",
    'allweapons': "Show all weapons",
    'buygrenade': "Buy Grenades",
}

gun = Guns("Gun", 10, -1, 1)
shotgun = Guns("Shot Gun", 25, 250, 2)
submachinegun = Guns("Sub Machine Gun", 50, 500, 3)
rifle = Guns("Rifle", 100, 1000, 4)
machinegun = Guns("Machine Gun", 250, 5000, 5)
guns = [gun, shotgun, submachinegun, rifle, machinegun]
grenade = Grenade("Grenade", 50, 25)
player = Player("Player", gun, grenade, Commands)
dragon = Dragon(1, 100,100, 5)


