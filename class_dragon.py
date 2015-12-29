from random import randint
class Dragon(object):
    def __init__(self, level, health, damage):
        self.level = level
        self.name = "Dragon"
        self.health = health
        self.damage = damage
    
    def do_damage(self, player):
        if player.evade()==1:
            print player.get_name()+" evades"
        else:
            player.health = player.health - self.damage
        
        
    def evade(self):
        if randint(1,3)==1:
            return 0
        else:
            return 1
