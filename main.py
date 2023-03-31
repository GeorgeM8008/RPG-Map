                                   #George Mi, CS30, March 
#This is a simple map for an RPG game


#These are variables of the different rooms in the lists below
row = 3
col = 0
Loop = True

inventory = []

def Get_Item():
    global inventory, row, col
    if row == 0 and col == 1 or row == 2 and col == 2:
        choice3 = input("Choice: ")
        if choice3 == "Yes":
            inventory.append("Medkit")
            print("You picked up the Medkit")
        elif choice3 == "No":
            print("You did not pick up the Medkit")
        else:
            print("I didn't understand that")
            Get_Item()
        
    
  

#Lists containing layout of the different rooms in the map
layout = [['Enemy Room', 'Supply Room', 'Safe Room', 'Escape Pod'],
          ['Safe Room',  'Safe Room',  'Enemy Room', 'Safe Room'],
          ['Safe Room',  'Safe Room',  'Supply Room',  'Enemy Room'],
          ['Starting Room', 'Safe Room', 'Enemy Room', 'Safe Room'],]
Tile_Descriptions = {
    "Safe Room" : {
        "Description" : "Empty room",
        "Effect" : "None" },
    "Starting Room" : {
        "Description" : "Room you begin the game in",
        "Effect" : "None" },
    "Enemy Room" : {
        "Description" : "A room with an enemy inside",
        "Effect" : "You lose 2 health" },
    "Escape Pod" : {
        "Description" : "An escape pod at the end of the ship",
        "Effect" : "You win" },
    "Supply Room" : {
        "Description" : "You find a small storage room with a medkit hanging on the wall",
        "Effect" : "Do you choose to pick it up?",
        "Item" : "Medkit"
    }
}
#This function moves the player around based on their input
#This function also detects if a player is trying to go out of bounds and prevents them
def move():
    global row, col, Loop
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
            elif row == 0:
                print("You have hit a wall.\n")
        elif choice2 == "S":
            if row < 3:
                row += 1
            elif row == 3:
                print("You have hit a wall.\n")
        elif choice2 == "W":
            if col > 0:
                col -= 1
            elif col == 0:
                print("You have hit a wall.\n")
        elif choice2 == "E":
            if col < 3:
                col += 1
            elif col == 3:
                 print("You have hit a wall.\n")
        elif choice2 == "Quit":
            print("Quitting Game")
            Loop = False
        else:
            print("I didn't understand that\n")
    else:
      print("I didn't understand that\n")

      

#This will loop the code as long as Loop is true
while Loop == True:
    print(f"Location: {layout[row][col]}")
    print(f"{Tile_Descriptions[layout[row][col]]['Description']}")
    print(f"{Tile_Descriptions[layout[row][col]]['Effect']}\n")
    if row == 0 and col == 3:
        Loop = False
    move()
