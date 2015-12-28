class Player(object):
    def __init__(self, name, gun):
        self.name = name
        self.coins = 0
        self.health = 100
        self.max_health = 100
        self.weapon = gun
        
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