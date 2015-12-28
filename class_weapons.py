class Weapons(object):
    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price 
        
    def get_name(self):
        return self.name
    
    def get_damage(self):
        return self.damage