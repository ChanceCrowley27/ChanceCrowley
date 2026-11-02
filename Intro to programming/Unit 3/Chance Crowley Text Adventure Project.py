def adventure_begins():
    print("Act One\n")
    print("you wake up with no memory on a spaceship")
    print("1. Get up and look around")
    print("2. close your eyes to sleep")
    choice=input(">")
    if choice =="1":
        look_around()
    elif choice =="2":
        print("you wake up to your alarm")
        Waking()
    else:
        print("Invalid Choice try again")
        adventure_begins()

def Attack_creature_textbook():
    print("You attack the creature by throwing a textbook at it")
    ending_7()

def attack_creature():
    global screw_driver_weapon
    global textbook_weapon
    print("1.Attack creature with textbook")
    print("2. Attack creature with screwdriver")
    choice=input(">")
    if choice =="1" and textbook_weapon==True:
        Attack_creature_textbook()   
    elif choice =="2"and screw_driver_weapon==True:
        Attack_creature_screw_driver()
    else:
        print("Invalid Choice try again")
        attack_creature()

def pick_up_textbook_weapon():
    global textbook_weapon
    textbook_weapon=True
    attack_creature()

def ending_5():
    print(" One of the creatures hears you and runs toward your location leaping at you")
    print(""" 
    _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def attack_creature_1():
    print("you try and attack the creature but it notices you and you fail to kill it")
    print(""" 
     _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def sneaky_escape():
    print("Act 2: The Escape")
    global key_card
    key_card=False
    print("as the door slide opens you notice a creature eating something with its back to you")
    print("1. Attack the creature")
    print("2. sneaky escape")
    print("3. retreat to grab a weapon in the room")
    
    choice=input(">")
    if choice =="1":
        print("You attack the creature")
        attack_creature_1()
    elif choice =="2":
        print("You try to make a sneaky escape and yet you are too loud ")
        ending_5()
    elif choice =="3":
        print("you retreat into the room to grab a weapon")
        room()
    else:
        print("Invalid Choice try again")
        sneaky_escape()

def drawer():
    global key_card
    key_card=True
    if key_card==True:
        print("Theres a key card in the drawer")
        print("you move to the door")
        sneaky_escape()
    if key_card==False:
        print("there is nothing in the drawer")
        top_of_table_2()

def picking_lock():
    print("Theres nothing in your pockets and you dont know how to pick a lock")
    door()

def ending_1():
    print("Act 3: The End")
    print(" the door opens with a click")
    print(" you look into the hallway to see an alien devoring a person")
    print("In a panic you drop the screw driver and it hears")
    print("You are attacked and eaten alive")
    print("""
    _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""") 
    adventure_begins()

def ending_2():
    print("The textbook protected you from the main attack")
    print("but it doesnt stop the poison from reaching your heart giving you a heart attack")
    print(""" 
    _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def ending_6():
    print("The small creatures block your exits and there is no way out")
    print("""
    _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def escape_vent():
    print("You climb into the vent which is crawling with creatures")
    ending_6()

def safe_escape():
    print("Act 3: THE END?")
    print("You smash the eggs put the boots on escape into space")
    print("You push off the station into space")
    print("as you float through space you reflect on what had just occured")
    print("You crash land on the planet below but the suit protects your fall")
    print("there you find a space ship and make your way back to earth")
    print("Once you arrive you relise you are the last human remaining")
    print("The creatures control the planet as well")
    print("THE END?")
    adventure_begins() 

def space_escape_2():
    print("As you suit up you look for your boots\n as you find them in the corner you notice that theirs something in them\n there are eggs in them")
    print("1. make an omelet")
    print("2. continue with the mission and just smash them")
    choice=input(">")
    if choice =="1":
        print("You make an omlet and then get the suit on")
        safe_escape()
    elif choice =="2":
        safe_escape()   
    else:   
        print("Invalid Choice try again")
        space_escape_2()

def Moon_Walk_Area():
    print("You enter the Moon walk area where you can see 3 suits on the wall and a hatch with a red button to the outside")
    print("1. grab a suit and jump into space")
    print("2. jump into space")
    choice=input(">")
    if choice =="1":
        print("You put on the suit and jump into space")
        space_escape_2()
    elif choice =="2":
        print("You slowly sufficate in space ")
        print("""                                                                                                                                                                                                
         _______  _______  __   __  _______    _______  __   __  _______  ______   
        |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
        |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
        |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
        |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
        |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
        |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
        adventure_begins()
    else:
        print("Invalid Choice try again")
        Moon_Walk_Area()

def The_Executor():
    print("Act 3: The End")
    print("You make a safe escape with enough supplies to last a few months")
    adventure_begins()

def USCSS_Nostromo():
    print("Act 3: The End?")
    print("As you board you notice the reminents of another speices")
    print("When you take off you hear a shrieking scream come from the engine area")
    print("you go to investigate and you are attacked from the ceiling and in the dark you make out a black figure in the darkness")
    print(""" 
    _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def UNSC_Infinity():
    print("Act 3: The End?")
    print("As you take off something happens to the engines and you barely leave the hangar before the engines quite and you start to crash toward the planet below")
    print(""" 
    _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def steal_ship():
    print("You see three ships in the hanger")
    print("1. The Executor")
    print("2. USCSS Nostromo")
    print("3. UNSC Infinity")
    choice=input(">")
    if choice =="1":
        print("You steal the Executor")
        The_Executor()
    elif choice =="2":
        print("You steal USCSS Nostromo")
        USCSS_Nostromo()
    elif choice =="3":
        print("You steal UNSC Infinity")
        UNSC_Infinity()
    else:
        print("Invalid Choice try again")
        steal_ship()

def find_weapon():
    print("You open the weapons cache only to see that its one of the creatures nests")
    print("you are overcome with many baby creatures and fail to grab a weapon")
    print(""" 
    _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def Shuttle_Area():
    print("you have come to the shuttle area")
    print("1. steal a ship and attempt to flee")
    print("2. Find a Weapon and take back the ship")
    choice=input(">")
    if choice =="1":
        print("You attempt to steal a ship to escape")
        steal_ship()
    elif choice =="2":
        print("You start to look around for a weapon")
        find_weapon()
    else:
        print("Invalid Choice try again")
        Shuttle_Area()

def escape_door():
    print("You have escaped the room thorugh the hallway you see more of these creatures")
    print("Above you are signs that indicate the shuttle launch area and the moon walk area")
    print("1.Run towards shuttle area")
    print("2.Run towards moon walk area")
    choice=input(">")
    if choice =="1":
        print("You run towards the shuttle area")
        Shuttle_Area()
    elif choice =="2":
        print("You run towards the moonwalk area")
        Moon_Walk_Area()
    else:
        print("Invalid Choice try again")
        escape_door()

def escape():
    print("Act 2: The Escape")
    print("you notice two exits the door or the airvent")
    print("1. escape through the door")
    print("2. escape through the airvent")
    choice=input(">")
    if choice =="1":
        print("You throw the book at the creature")
        escape_door()
    elif choice =="2":
        escape_vent()
    else:
        print("Invalid Choice try again")
        escape()

def read_textbook():
    global textbook
    print("You begin to read Monstourous Creatures by C. Dallin")
    print("as you read you learn about the creatures that habit the planets near you")
    print("As you read one of these creatures makes its way quietly out an air vent near you")
    print("At the last second you hear it behind you")
    print("1. throw the textbook at it")
    print("2. Attempt to flee while keeping the book")
    choice=input(">")
    if choice =="1":
        print("You throw the book at the creature")
        print("disoriented it crashes through the door breaking it and killing the creature outside")
        textbook=False
        escape()
    elif choice =="2":
        print("You are too slow and the creature catchs you stabbing you with long tendrals")
        textbook=True
        ending_2()
    else:
        print("Invalid Choice try again")
        read_textbook()

def top_of_table():
    global screw_driver
    print("you look on top of the table\n on your left there is a screw driver and to your right there is a textbook on alien spieces")
    print("1. pick up the screw driver") 
    print("2. pick up the textbook")  
    choice=input(">")
    if choice =="1":
        print("you pick up the screw driver and walk towards the door")
        screw_driver= True
        door()
    elif choice =="2":
        print("you pick up the textbook")
        read_textbook() 
    else:
        print("Invalid Choice try again")
        top_of_table()  

def table():
    print("you start to look at the table")
    print("1. Look in drawer")
    print("2.look on top of table")
    choice=input(">")
    if choice =="1":
        print("you look in the drawer")
        drawer()
    elif choice =="2":
        top_of_table()
    else:
        print("Invalid Choice try again")
        table()

screw_driver=False

def door():
    print("As you approach the door you see a key card slot")
    print("1. Attempt to pick the lock with what ever you have in your pockets")
    print("2. Attempt to look for anything at the table")
    print("3. Use Screw driver")
    choice=input(">")
    if choice =="1" or picking_lock==False:
        picking_lock()
    elif choice =="2":
        print("you walk towards the table")
        table()
    elif choice =="3" and screw_driver == True:
        print("you use the screw driver and the door opens")
        ending_1()
    elif choice =="3" and screw_driver == False:
        print("wheres the screwdriver")
        table()
    else:
        print("Invalid Choice try again")
        door() 

def look_around():
    print("You get up and start to look around")
    print("To the left of you there is a table with a drawer below and to your right is a futuristic door")
    print("1. go towards the table")
    print("2. go towards the door")
    choice=input(">")
    if choice =="1":
        table()
    elif choice =="2":
        print("you move towards the door")
        door()
    else:
        print("Invalid Choice try again")
        look_around()
         
def ending_3():
    print("Act 3:The End")
    print("you fall back to sleep and sleep for Eternity")
    print("""                                                                                                                                                                                                    
    _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def Waking():
    print("You wake up in your bed to your alarm before work")
    print("1.Go back to sleep")
    print("2.Go to Work")
    choice=input(">")
    if choice =="1":
        ending_3()
    elif choice =="2":
        print("you wake up to your alarm")
        work()    
    else:
        print("Invalid Choice try again")
        Waking()

def work():
    print("you go to work and something feels off but it isnt till you get there that you realise the building is desolate and in disrepair\n As you slowly make your way up the stairs you see a large grotesk creature looming around the room")
    print("1. Run away")
    print("2. slowly creep away")
    choice=input(">")
    if choice =="1":
        print("As you run away the creature spots you and shoots a spike at you")
        ending_4()
    elif choice =="2":
        print("you slowly creep away")
        sneak_away() 
    else:
        print("Invalid Choice try again")
        work()

def ending_4():
    print("you immediatly lose all feeling in your body and the creature stomps towards you, grabs you and you are slowly eaten piece by piece")
    print("""                                                                                                                                                                                                
     _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def sneak_away():
    print("The creature spots you and chases you down")
    print(""" 
     _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def pick_up_screw_driver_weapon():
    global screw_driver_weapon
    screw_driver_weapon=True
    attack_creature()

def top_of_table_2():
    print("you look on top of the table\n on your left there is a screw driver and to your right there is a textbook on alien spieces")
    print("1. pick up the screw driver") 
    print("2. pick up the textbook")  
    choice=input(">")
    if choice =="1":
        print("you pick up the screw driver and walk towards the door")
        pick_up_screw_driver_weapon()
    elif choice =="2":
        print("you pick up the textbook and head towards the ")
        pick_up_textbook_weapon() 
    else:
        print("Invalid Choice try again")
        top_of_table_2()

def attack_creature_rifle():
    print("you shoot the creature and it dies and you throw the rifle to the side")
    escape_door()

def look_around_bed():
    print("as you look around the bed you notice something under the bed")
    print("1.Grab item")
    print("2.Grab the pillow")
    choice=input(">")
    if choice =="1":
        print("You find a rifle under the bed")
        attack_creature_rifle()   
    elif choice =="2":
        print("you grab the pillow and relise it will do nothing against the creature and you throw it to the side")
        room()
    else:
        print("Invalid Choice try again")
        look_around_bed()

def room():
    print("1. walk to the table")
    print("2. Look around the bed")
    choice=input(">")
    if choice =="1":
        print("You walk up to the table")
        top_of_table_2()   
    elif choice =="2":
        look_around_bed()
    else:
        print("Invalid Choice try again")
        room()

def ending_7():
    print("The textbook bounces off of the creature as it slowly turns around and lunges at you")
    print("""
     _______  _______  __   __  _______    _______  __   __  _______  ______   
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n""")
    adventure_begins()

def Attack_creature_screw_driver():
    print("You stab the creature in the eye and it runs off")
    escape_door()

adventure_begins()