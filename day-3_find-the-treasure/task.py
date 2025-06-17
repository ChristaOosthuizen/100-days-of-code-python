print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

import time

print("Welcome to Treasure Island.\n")
time.sleep(1)
print("Your mission is to find the treasure.\n")

time.sleep(1)
choice1 = input('Do you want to go left or right? '
                  'Enter "L" or "R" \n ').upper()

time.sleep(1)
if choice1 == "L":
    choice2 = input('Do you want to swim or wait? '
                   'Enter "S" or "W"\n ').upper()
    time.sleep(1)
    if choice2 == "W":
        choice3 = input('Patience usually pays off, good choice! '
                        'Do you want to go into the Red, Yellow or Blue Door? '
                     'Enter "R", "Y" or "B" \n').upper()
        time.sleep(1)
        if choice3 == "Y":
            print("You win! Great job!!")
        elif choice3 == "R":
            print("Game Over! You got burnt by a raging fire")
        elif choice3 == "B":
            print("Game Over! You got eaten by a scary monster")
        else:
            print("Game Over! You did not enter a valid option"
                  "Read the instructions and try again")

    else:
        time.sleep(1)
        print("Game Over! You were eaten by Piranhas!")

else:
    time.sleep(1)
    print("Game Over! You entered a portal and can never return!")