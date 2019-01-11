from sys import exit
from textwrap import dedent

bullet = True
first_start = True
first_gate = True
hasBullets = True
bullets = 6
first_house = True
first_woods = True
first_shack = True

def start_room():
    global first_start
    global bullets
    global hasBullets
    good = True
    if first_start:
        print("What will you do?")
        first_start = False
    elif first_start == False:
        print("Starting room")
    
    choice = input("> ")
    while good: 
        if (choice == "pick up bullets" or choice == "take bullets") and bullet == True:
            bullets = 6
            hasBullets = False
            
            print("taken")
            choice = input("> ")
            
        elif(choice == "pick up bullets" or choice == "take bullets") and bullet == False:
            print("You already have the bullets.")
            
            choice = input("> ")
            
        elif choice == "go north" or choice == "walk north":
            gate()
        
        elif choice == "go south" or choice == "walk south":
            house()
            
        elif choice == "go east" or choice == "walk east":
            shack()
            
        elif choice == "go west" or choice == "walk west":
            woods()
        
        elif choice == "look around":
            print(dedent("""
            Trees around you have slashes on them and it gives you 
            an eerie feeling. You look around and there are 
            paths north, south, east and west.
            """))
        else:
            print("I dont know what that means")
        
        choice = input("> ")
            
            

def gate():
    global first_gate
    good = True
    if first_gate:
        print(dedent("""
        You walk north and there is a wall about 15ft 
        made out of concrete. There is a door but it 
        is locked. It seems that you need a keycard 
        do unlock the door. Where the keycard is you
        have no idea. You can't go north, east, west.
        The only way you could go is back south.
        """))
        
        first_gate = False
    else:
        print("Gate")
    while good:
        choice = input("> ")
        if choice == "go south" or choice == "walk south":
            start_room()
        else:
            print("I dont know what that means.")
            choice = input("> ")
        
    

def house():
    global first_house
    good = True
    if first_house:
        print(dedent("""
        You walk south and see what seems to be an
        abandoned house. You go up to the front door
        and it's locked. There's a cracked window
        that leads to inside the house. There is 
        a forest all around you except from the 
        way you came, north.
        """))
        first_house = False
    else:
        print("House")
    
    while good:
        choice = input("> ")
        
        if choice == "go north" or choice == "walk north":
            start_room()
        else:
            print("I don't know what that means")
    

def woods():
    global first_woods
    good = True
    if first_woods:
        print(dedent("""
        You walk west and find yourself deep in the forest.
        You hear noises and feel some dark presence in the
        forest. You start to think that you are being 
        watch. There is a path south of where you are and
        the path you just came from, east.
        """))
        first_woods = False
        
    else:
        print("Woods")
    
    while good:
        choice = input("> ")
        
        if choice == "go east" or choice == "walk east":
            start_room()
        else:
            print("I dont know what that means.")
            choice = input("> ")
    
    
    

def shack():
    global first_shack
    good = True
    if first_shack:
        print(dedent("""
        As you walk east you see a small litle shack in the 
        distance. When you get to the shack you see that 
        there is no door to the shack. There seens to be 
        nothing wrong with the shack. The only path
        around you is the path you took to get to the 
        shack, west.
        """))
        first_shack = False
    else:
        print("Shack")
    
    while good:
        choice = input("> ")
        
        if choice == "go west" or choice == "walk west":
            start_room()
        else:
            print("I dont know what that means.")
            choice = input("> ")
    
   


print("""
You're driving on the highway and realize that for
some reason the route you usually take is different. 
Out of nowhere the car you're in gets hit by some
invisible force and get into a serious accident which
leaves you unconscious. When you regain consciousness
you seem to be in the middle of the woods. Trees 
around you have slashes on them and it gives you 
an eerie feeling. You look around and there are 
paths north, south, east and west. There's a 
flashlight below you and 6 bullets but no gun.
""")



start_room()
    
    


