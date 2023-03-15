#George Mi, CS30, March 
#This is a simple map for an RPG game


#These are variables of the different rooms in the lists below
row = 3
col = 0
Loop = True


#Lists containing layout of the different rooms in the map
layout = [['Enemy Room', 'Supply Room', 'Safe Room', 'Escape Pod'],
          ['Safe Room',  'Safe Room',  'Enemy Room', 'Safe Room'],
          ['Safe Room',  'Safe Room',  'Safe Room',  'Enemy Room'],
          ['Starting Room', 'Safe Room', 'Enemy Room', 'Safe Room'],]


#This function moves the player around based on their input
#This function also detects if a player is trying to go out of bounds and prevents them
def move():
    global row, col, Loop
    print("Options for movement:\nN, S, E, W\n")
    print("Options for action:\nQuit\n")    
    choice =input("Action: ")
    if choice == "N":
        if row > 0:
            row -= 1
        elif row == 0:
            print("You have hit a wall.")
            row = 0
        


        
    elif choice == "S":
        if row < 3:
            row += 1
        elif row == 3:
            print("You have hit a wall.")


        
    elif choice == "W":
        if col > 0:
            col -= 1
        elif col == 0:
            print("You have hit a wall.")


        
    elif choice == "E":
        if col < 3:
            col += 1
        elif col == 3:
            print("You have hit a wall.")



    elif choice == "Quit":
         Loop = False



    else:
      print("I didn't understand that\n")


while Loop == True:
  print(f"Location: {layout[row][col]}\n")
  move()