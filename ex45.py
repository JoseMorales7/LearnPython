from sys import exit
from textwrap import dedent

bullets = 0
bullet = False
flashlight = False
first_start = True
first_gate = True
first_house = True
first_woods = True
first_open_field = True
first_shack = True

def start_room():
    global first_start
    global bullet
    global flashlight
    good = True
    
    if first_start:
        print("What will you do?")
        first_start = False
    elif first_start == False:
        print("Starting room")
    
    choice = input("> ")
    while good: 
        if (choice == "pick up bullets" or choice == "take bullets") and bullet == False:
            bullets = 6
            bullet = True
            
            print("taken")
            choice = input("> ")                    ## whenever take bullets and press enter it does the function but 
                                                    ## when you type something after it wont register. So have to type again
                                                    ## Its the same with the flashlight.
            
        elif (choice == "pick up bullets" or choice == "take bullets") and bullet == True:
            print("You already have the bullets.")
            
            choice = input("> ")
            
        elif (choice == "pick up flashlight" or choice == "take flashlight") and flashlight == False:
            flashlight = True
            
            print("taken")
            choice = input("> ")
        
        elif (choice == "pick up flashlight" or choice == "take flashlight") and flashlight == True:
            print("You already have the flashlight.")
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
        elif choice == "look around":
            print(dedent("""
            The big wall is still there and you need
            the keycard to get through the door. 
            Good luck with that. The only way you 
            could go is south.
            """))
            
        elif (choice == "go north") or (choice == "go west") or (choice == "go east"):
            print("Can't go that way dummy.")
            
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
            
        elif choice == "look around":
            print(dedent("""
            The house has a cracked window which seems 
            like you could break. *COUGH* *COUGH*
            The only path is to the north.
            """))
        
        elif (choice == "go south") or (choice == "go east") or (choice == "go west"):
            print("You can't go that way dum dum.")
            
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
            
        elif choice == "go south" or choice == "walk south":
            open_field()
            
        elif choice == "look around":
            print(dedent("""
            You're currently deep in the woods and you
            have a feeling you're being watched. The
            only paths are south and east to where
            you came.
            """))
            
        elif (choice == "go north") or (choice == "go west"):
            print("Wrong way dum dum")
            
        else:
            print("I dont know what that means.")
            choice = input("> ")
    

def open_field():
    global first_open_field
    good = True
    
    if first_open_field:
        print(dedent("""
        You walk south of the woods and arrive at an open
        field of grass. A few miles away is the wall 
        surrounding the entire area you're in. There 
        seems to be nothing around but grass around you.
        The only path is back north.
        """))
        
        first_open_field = False
    else:
        print("Open Field")
    
    choice = input("> ")
    
    while good:
        if choice == "go north" or choice == "walk north":
            woods()
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
            
        elif choice == "look around":
            print(dedent("""
            The shack has no door. Maybe you should
            go in. Dumb dumb. The only path is to 
            the west.
            """))
            
        elif (choice == "go north") or (choice == "go east") or (choice == "go south"):
            print("No not that way silly.")
            
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
    
    


