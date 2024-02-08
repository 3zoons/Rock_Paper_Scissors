from random import randint

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

game_image = [rock, paper, scissors]

#User Choice 
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_image[user_choice])

#Computer Choice
print("Computer's Choice")
computer_choice = randint(0, 2)
print(game_image[computer_choice])

#Logic
if user_choice >= 3 or user_choice < 0 :
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2 : 
    print("You win!")
elif computer_choice == 0 and user_choice == 2 : 
    print("You lose!")
elif user_choice > computer_choice : 
    print("You win!")
elif computer_choice > user_choice : 
    print("You lose!")
elif user_choice == computer_choice : 
    print("Draw!")
