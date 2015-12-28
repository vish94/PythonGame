class Dragon(object):
    def __init__(self, level, health):
        self.level = level
        self.name = "Dragon"
        self.health = health
        self.damage = 5
    
    def do_damage(self, player):
        player.health = player.health - self.damage
