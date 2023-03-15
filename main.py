#George Mi, CS30, March 10


row = 3
col = 0


layout = [['Enemy Room', 'Supply Room', 'Safe Room', 'Escape Pod'],
          ['Safe Room',  'Safe Room',  'Enemy Room', 'Safe Room'],
          ['Safe Room',  'Safe Room',  'Safe Room',  'Enemy Room'],
          ['Starting Room', 'Safe Room', 'Enemy Room', 'Safe Room'],]


def move():
    global row, col
    print("Options for movement:\nN, S, E, W\n")
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
        #while choice == "Go North" or "go north" or "go south" or "Go South" or "go west" or "Go West" or "explore" or "attack" or "defend" or "quit" or "Quit":
           # move()


        
    elif choice == "W":
        if col > 0:
            col -= 1
        elif col == 0:
            print("You have hit a wall.")
        #while choice == "Go North" or "go north" or "go south" or "Go South" or "go west" or "Go West" or "explore" or "attack" or "defend" or "quit" or "Quit":
          #  move()


        
    elif choice == "E":
        if col < 3:
            col += 1
        elif col == 3:
            print("You have hit a wall.")
       # while choice == "Go North" or "go north" or "go south" or "Go South" or "go west" or "Go West" or "explore" or "attack" or "defend" or "quit" or "Quit":
           # move()



while True:
  print(f"Location: {layout[row][col]}\n")
  move()
  