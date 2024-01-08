#Rock,Paper,Scissor game

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

game_images=[rock,paper,scissors]

userchoice=int(input("Enter your choice 1 for rock, 2 for paper and 3 for scissor\n"))
if userchoice<1 or userchoice>3:
    print("Enter a valid choice")
else:
    print(game_images[userchoice-1])
    computer_choice=random.randint(1,3)
    print("Computer's Choice\n")
    print(game_images[computer_choice-1])
    if userchoice==1 and computer_choice==3:
        print("You Win!!!")
    elif computer_choice==1 and userchoice==3:
        print("You Loose")
    elif userchoice>computer_choice:
        print("You Win!!!")
    elif computer_choice>userchoice:
        print('You Loose')
    elif userchoice==computer_choice:
        print("It's a draw")

