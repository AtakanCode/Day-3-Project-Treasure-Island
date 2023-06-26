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

Left_right=input("You are at a cross road,which way you will go? left or right ")

if Left_right=="L":
  swim_wait=input("You come to a lake. There is an island in the middle of the lake, What you gonna do? You can 'swim' to swim across or you can 'wait' for the boat.")
  if swim_wait=="W":
    door=input("You arrived at the island unharmed. There is a house with 3 doors. Which door will you choose? Red, Blue or Yellow ")
    if door=="Y":
      print("You entered room of treause, You have won, congrats!!")
    elif door=="B":
      print("You are eaten by beasts, game over, have fun of the pain, game over")
    elif door=="R":
      print("You are burnt by fire, now you are cooked really well, game over")
    else:
      print("Game over")
  else:
    print("You are attacked by traut, game over")
else:
  print("You fell into a hole game over")
  
    
  
