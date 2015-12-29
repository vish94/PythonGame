from initialize import *

print "Enter your name?"
name = raw_input("> ")
player.set_name(name)

print "Welcome "+player.get_name()+"! Ready to face this Python adventure? Fight with the dragon till you survive!"
player.status()
print "Write 'help' to see all the valid keys"
player.do_damage(1, dragon)
player.do_damage(2, dragon)