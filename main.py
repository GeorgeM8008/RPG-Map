#George Mi, CS30, March 
#This is a simple map for an RPG game


#These are variables of the different rooms in the lists below
row = 3
col = 0
Loop = True
Keys = False

#Empty list for inventory
inventory = []

#This function detects if you are in a room with an item and gives the choice to pick it up
def Get_Item():
    global inventory, row, col, Keys
    if row == 0 and col == 1:
        print(f"\n{items[layout[row][col]]['Item']}")
        choice3 = input("Choice: ")
        if choice3 == "Yes":
            inventory.append("Medkit")
            print("\nYou picked up the Medkit\n")
            move()
        elif choice3 == "No":
            print("\nYou did not pick up the Medkit\n")
            move()
        else:
            print("\nI didn't understand that")
            Get_Item()
    elif row == 2 and col == 2:
        print(f"\n{items[layout[row][col]]['Item']}")
        choice4 = input("Choice: ")
        if choice4 == "Yes":
            inventory.append("Keys")
            print("\nYou picked up the keys\n")
            Keys = True
            move()
        elif choice4 == "No":
            print("\nYou did not pick up the keys\n")
            move()
#This function detects if you are on the end tile with the keys, thus winning the game
def Win():
    global Loop, Keys
    if row == 0 and col == 3 and Keys == True:
        Loop = False
    elif row == 0 and col == 3 and Keys == False:
        print("You find an empty escape pod but there's no key for the ignition")
        move()
    
  

#Lists containing layout of the different rooms in the map
layout = [['Enemy Room', 'Supply Room', 'Safe Room', 'Escape Pod'],
          ['Safe Room',  'Safe Room',  'Enemy Room', 'Safe Room'],
          ['Safe Room',  'Safe Room',  'Janitor Closet',  'Enemy Room'],
          ['Starting Room', 'Safe Room', 'Enemy Room', 'Safe Room'],]
#Nested dictionaries describing the rooms and their effects
Tile_Descriptions = {
    "Safe Room" : {
        "Description" : "You enter an empty room",
        "Effect" : "You ponder your next actions" },
    "Starting Room" : {
        "Description" : "You find yourself on an enemy ship and must escape"},
    "Enemy Room" : {
        "Description" : "You enter room with an enemy inside",
        "Effect" : "You lose 2 health" },
    "Escape Pod" : {
        "Description" : "You find a lone escape pod at the end of the ship",
        "Effect" : "You win" },
    "Supply Room" : {
        "Description" : "You find a small storage room with a Medkit hanging on the wall",
        "Effect" : "Do you choose to pick it up?" },
    "Janitor Closet" : {
        "Description" : "You find a small janitor's closet with a pair of keys dangling off a key hook",
        "Effect" : "Do you choose to pick it up?",
    }
}

#Nested dictionary of all the items 
items = {
    "Safe Room" : {
        "Item" : "None" },
    "Starting Room" : {
        "Item" : "None" },
    "Enemy Room" : {
        "Item" : "None" },
    "Supply Room" : {
        "Item" : "Medkit" },
    "Janitor Closet" : {
        "Item" : "Keys" }
    } 
 
#This function moves the player around based on their input
#This function also detects if a player is trying to go out of bounds and prevents them
def move():
    global row, col, Loop, inventory
    print("Options for action:\nQuit, Move, Inventory\n")    
    choice = input("Action: ")
    if choice == "Quit":
        print("Quitting Game")
        Loop = False
    elif choice == "Move":
        print("Options for movement:\nN, S, E, W\n")
        choice2 = input("Action: ")
        if choice2 == "N":
            if row > 0:
                row -= 1
                print(f"\n{Tile_Descriptions[layout[row][col]]['Description']}")
                print(f"{Tile_Descriptions[layout[row][col]]['Effect']}\n")
            elif row == 0:
                print("\nYou have hit a wall.\n")
        elif choice2 == "S":
            if row < 3:
                row += 1
                print(f"\n{Tile_Descriptions[layout[row][col]]['Description']}")
                print(f"{Tile_Descriptions[layout[row][col]]['Effect']}\n")
            elif row == 3:
                print("\nYou have hit a wall.\n")
        elif choice2 == "W":
            if col > 0:
                col -= 1
                print(f"\n{Tile_Descriptions[layout[row][col]]['Description']}")
                print(f"{Tile_Descriptions[layout[row][col]]['Effect']}\n")
            elif col == 0:
                print("\nYou have hit a wall.\n")
        elif choice2 == "E":
            if col < 3:
                col += 1
                print(f"\n{Tile_Descriptions[layout[row][col]]['Description']}")
                print(f"{Tile_Descriptions[layout[row][col]]['Effect']}\n")
            elif col == 3:
                 print("\nYou have hit a wall.\n")
        elif choice2 == "Quit":
            print("Quitting Game")
            Loop = False
        else:
            print("I didn't understand that\n")

    elif choice == "Inventory":
        if len(inventory) == 0:
            print("Your inventory is empty")
        else:
            for item in inventory:
                print(f"-{item}")
    else:
      print("\nI didn't understand that\n")

      

#Introduction to situation
print(f"{Tile_Descriptions[layout[row][col]]['Description']}\n")
#This will loop the code until they win the game or quit
while Loop == True:
   Get_Item()
   move()
   Win()