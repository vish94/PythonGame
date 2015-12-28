class Dragon(object):
    def __init__(self, level, health, damage):
        self.level = level
        self.name = "Dragon"
        self.health = health
        self.damage = damage
    
    def do_damage(self, player):
        player.health = player.health - self.damage
