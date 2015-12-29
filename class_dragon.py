from random import randint
class Dragon(object):
    def __init__(self, level, health, max_health, damage):
        self.level = level
        self.name = "Dragon"
        self.health = health
        self.max_health = max_health
        self.damage = damage
        print "You are attacked by the first dragon. Health: 100. Damage: 5"
    
    def do_damage(self, player):
        if player.evade()==1:
            print player.get_name()+" managed to escape the dragon breath!"
        else:
            player.health = player.health - self.damage
            print "Ahhh! You took damage"
            print "Your health: "+ str(player.get_health()) + " of " + str(player.get_max_health())
    
    def get_health(self):
        return self.health
    
    def get_damage(self):
        return self.damage
    
    def get_level(self):
        return self.level
    
    def get_max_health(self):
        return self.max_health
        
        
    def evade(self):
        if randint(1,4)==1:
            return 1
        else:
            return 0
    
    def nextdragon(self):
        self.level = self.level + 1
        self.max_health = self.max_health + 50
        self.health = self.max_health
        self.damage = self.damage + 1
        print "You are attacked by the next dragon. Health: "+str(self.get_health())+" .Damage: "+str(self.get_damage())
