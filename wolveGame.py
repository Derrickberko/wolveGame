print('''
*******************************************************************************
                   |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
snd  || ||             '-'
     '-''-'
*******************************************************************************
''')
print("Welcome to the Chase game.")
print("Your mission is to escape from the Wolve")

#Write your code below this line 👇

choice1 = input('You are jogging in the bush and you came accross this wolve. Would you run or fight? Type "run" or "fight" \n').lower()

if choice1 == "run":
  choice2 = input('Now you escaped but You\'ve come to a lake. The Wolve is still on you. Would you swim or wait. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  
  if choice2 == "wait":
    choice3 = input("Now that you escaped. You arrived at a house. You entered and now you want to rest. There is  3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the bed you can rest on! You Win!")
    elif choice3 == "blue":
      print("You enter a room of Vimpires. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
