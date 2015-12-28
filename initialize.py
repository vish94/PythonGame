from class_weapons import Weapons
from class_player import Player
from class_dragon import Dragon

Commands = {
    'quit' : Player.exitgame,
    'help' : Player.askhelp,
    #'status' : Player.status,
}

gun = Weapons("Gun", 10, -1)
player = Player("Player", gun, Commands)
dragon = Dragon(1, 100, 5)


