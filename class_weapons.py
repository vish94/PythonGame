class Weapons(object):
    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price 
        
    def get_name(self):
        return self.name
    
    def get_damage(self):
        return self.damage
        
    def do_damage(self, player, dragon):
        dragon.health = dragon.health - self.damage
        
        
class Guns(Weapons):
    def __init__(self, name, damage, price):
        Weapons.__init__(self, name, damage, price)
        
    def do_damage(self, player, dragon):
        Weapons.do_damage(self, player, dragon)
        dragon.do_damage(self, player)
        
        
        
class Grenade(Weapons):
    def __init__(self, name, damage, price):
        Weapons.__init__(self, name, damage, price)
        self.count = 0
        
    def do_damage(self, player, dragon):
        Weapons.do_damage(self, player, dragon)
        print "Dragon skipped"
    
    def get_count(self):
        return self.count