class Player(object):
    def __init__(self, name, gun, commands):
        self.name = name
        self.coins = 0
        self.health = 100
        self.max_health = 100
        self.weapon = gun
        self.commands = commands
    
    def set_name(self, name):
        self.name = name
        
    def get_health(self):
        return self.health
    
    def get_coins(self):
        return self.coins
        
    def get_max_health(self):
        return self.max_health
        
    def do_damage(self, dragon):
        dragon.health = dragon.health - self.weapon.damage
        
    def change_weapon(self, weapon):
        self.weapon = weapon
        
    def askhelp(self):
        print self.commands.keys()
    
    def exitgame(self):
        print "You were eaten by the dragon!"
        quit()
        
    def status(self):
        print "Health: " + str(self.get_health()) + " of " + str(self.get_max_health())
        print "Coins: " + str(self.get_coins())
        print "Weapon name: " + self.weapon.get_name() + "  Damage: " + str(self.weapon.get_damage())
