import random

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

game_images = [rock, paper, scissors]

userInput = int(input("Hey, user choose a number 0 for Rock, 1 for Paper or 2 for Scissors "))
print(f"user choose {userInput } ")
print(game_images[userInput])

computerInput = random.randint(0 , 2)
print(game_images[computerInput])
print(f"computer choose {computerInput}")

if userInput>= 3 or userInput < 0: 
  print("You typed an invalid number, you lose!") 
elif userInput == 0 and computerInput  == 2:
  print("You win!")
elif computerInput  == 0 and userInput == 2:
  print("You lose")
elif computerInput  > userInput:
  print("You lose")
elif userInput> computerInput :
  print("You win!")
elif computerInput  == userInput:
  print("It's a draw")