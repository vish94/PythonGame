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
    
    def get_price(self):
        return self.price
    
    def show_information(self, num):
        print "Weapon Name: "+self.name+". Damage: "+str(self.damage)+". Price: "+str(self.price)+". Type "+str(num)+" to buy"
    
    def buy(self, player):
        if player.weapon.level < self.level and player.coins > self.price :
            player.coins = player.coins - self.price
            player.change_weapon(self)
            print "You have bought "+self.name
        else:
            print "You dont have enough coins to buy this weapon or you already have a better weapon"
        
        
class Guns(Weapons):
    def __init__(self, name, damage, price, level):
        Weapons.__init__(self, name, damage, price)
        self.level = level
        
    def do_damage(self, player, dragon):
        Weapons.do_damage(self, player, dragon)
        
        
class Grenade(Weapons):
    def __init__(self, name, damage, price):
        Weapons.__init__(self, name, damage, price)
        self.count = 0
        
    def do_damage(self, player, dragon):
        Weapons.do_damage(self, player, dragon)
        self.count = self.count - 1
    
    def get_count(self):
        return self.count

            