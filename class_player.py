from random import randint
class Player(object):
    def __init__(self, name, gun, grenade, commands):
        self.name = name
        self.coins = 0
        self.health = 100
        self.max_health = 100
        self.weapon = gun
        self.grenades = grenade
        self.commands = commands
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_health(self):
        return self.health
    
    def get_coins(self):
        return self.coins
        
    def get_max_health(self):
        return self.max_health
        
    def change_weapon(self, weapon):
        self.weapon = weapon
        
    def askhelp(self):
        print self.commands.keys()
    
    def exitgame(self):
        print "You were eaten by the dragon!"
        quit()
        
    def do_damage(self, num, dragon):
        if num==1:
            if dragon.evade()==1:
                print "Dragon evades"
            else:
                self.weapon.do_damage(self, dragon)
        else:
            if self.grenades.get_count() > 0:
                self.grenades.do_damage(self, dragon)
            else:
                print "You dont have anough grenades. Dragon attacks."
    
    def evade(self):
        if randint(1,3)==1:
            return 1
        else:
            return 0
        
    def status(self):
        print "Health: " + str(self.get_health()) + " of " + str(self.get_max_health())
        print "Coins: " + str(self.get_coins())
        print "Weapon name: " + self.weapon.get_name() + "  Damage: " + str(self.weapon.get_damage())
        
    def attack(self):
        
