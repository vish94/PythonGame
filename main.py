from initialize import *

print "Enter your name?"
name = raw_input("> ")
player.set_name(name)

print "Welcome "+player.get_name()+"! Ready to face this Python adventure? Fight with the dragon till you survive!"
player.status(dragon)
print "Write 'help' to see all the valid keys"
level = 1
status = 0
while(player.get_health()>0):
    
    if(dragon.get_health()<=0):
        status = 0
        level = level + 1
        print "You killed the dragon. Now you will face the level: "+str(level)+" dragon!"
        dragon.nextdragon()
        
    else:    
        keyword = raw_input("> ")
        if(keyword=="help"):
            player.askhelp()
        elif(keyword=="status"):
            player.status(dragon)
        elif(keyword=="quit"):
            player.exitgame()
        elif(keyword=="attack"):
            player.attack(dragon)
        elif(keyword=="throwgrenade"):
            player.throwgrenade(dragon)
        elif(keyword=="allweapons"):
            for thisgun in guns:
                if thisgun.level>player.weapon.level:
                    thisgun.show_information(guns.index(thisgun))
            print "Type return to resume the game"
            weaponkey = raw_input(">> ")
            if(weaponkey=="return"):
                continue
            else:
                try:
                    weaponkey = int(weaponkey)
                except:
                    print "Not a valid input"
                    continue
                i = 0
                for thisgun in guns:
                    if i==weaponkey:
                        thisgun.buy(player)
                    i=i+1
        elif(keyword=="buygrenade"):
            
        else:
            print "I could not validate the keyword. Type help to see all valid keywords"
    