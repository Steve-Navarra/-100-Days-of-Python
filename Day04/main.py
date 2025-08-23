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

game_input = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

computer_input = random.randint(0,2)

if user_input >= 0 and user_input <= 2:
    print(game_input[user_input])

print("Computer chose:")
print(game_input[computer_input])

if user_input >= 3 or user_input < 0:
    print("You typed an invalid choice. You Lose")
elif user_input == 0 and computer_input == 2:
    print("You win!")
elif computer_input == 0 and user_input == 2:
    print("You Lose!")
elif computer_input > user_input:
    print("You lose!")
elif user_input > computer_input:
    print("You win")
elif user_input == computer_input:
    print("It's a draw!")
