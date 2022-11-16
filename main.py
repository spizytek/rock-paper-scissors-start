rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
#Rules 
#Rock wins against scissors
#scissors wins against paper 
#paper wins against rock
var = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper or 2 Scissors."))

if((var < 0) or (var >= 3)):
  print("You entered an invalid Command, you lose!")
else:
  gme_ls = [rock, paper ,scissors]
  cvar = random.randint(0,2)
  print(gme_ls[var])
  print("Computer chose")
  print((gme_ls[cvar]))


  if( (var == 0) and (cvar == 2) ):
  #you win
    print("You win")
  elif((cvar ) > (var ) ):
    print("You lose")
  elif((var ) > (cvar ) ):
    print("You win")
  elif((cvar  == 0) and (var == 2) ):
    print("You lose")
  elif((cvar) == (var) ):
    print("It's a draw ")

