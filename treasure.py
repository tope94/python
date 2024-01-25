print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You are at a Junction. Where do you want to turn to? Type 'left' or 'right'\n").lower()

if direction == "right":
          print("You got hit. GAMER OVER!")
elif direction == "left":
          swim_wait = input("You turned in a direction that takes you to a lake. There is an island in the middle of the lake. To wait for a boat, Type 'wait' . Type 'swim' to swim across.\n").lower()
          swim_wait_answer = print(f"You chose to {swim_wait}.")
          # print(swim_wait_answer)
          if swim_wait == "wait":
                    door = input("Now a boat picked you up from the lake and you've arrived at the island unharmed. On the island, there is a house with 3 doors. One red, One blue and one yellow. Which color do you choose?\n").lower()
                    door_answer = print(f"You chose the {door} door.")
                    # print(door_answer)
                    if door == "red":
                              print("BOOM! You've been Burned by Fire. GAME OVER!")
                    elif door == "blue":
                              print("BOOM! \U0001F604 You've been Eaten by Beasts. GAME OVER!")
                    elif door == "yellow":
                              print("Ding Ding Ding! You Win! You made it to the end of the game")
                    else:
                              print("Invalid color, GAME OVER!")
          else:
                    print("You got attacked by Sharks. GAME OVER!")
          

       