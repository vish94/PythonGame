from initialize import *

print "Enter your name?"
name = raw_input("> ")
player.set_name(name)

print "Welcome "+player.get_name()+"! Ready to face this Python adventure? Fight with the dragon till you survive!"
player.status()
print "Write 'help' to see all the valid keys"

while(player.get_health()>0):
    keyword = raw_input("> ")
    if(keyword=="help"):
        player.askhelp()
    elif(keyword=="status"):
        player.status()
    elif(keyword=="quit"):
        player.exitgame()
    else:
        print "I could not validate the keyword. Type help to see all valid keywords"
    