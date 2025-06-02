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

game = [rock, paper, scissors]
player = int(input("Choose between 0 - Rock, 1 - Paper or 2 - Scissors: "))
if player >= 0 and player <= 2:
    print(game[player])

pc_choice = random.randint(0, 2)
print("PC chose: ")
print(game[pc_choice])

if player >= 3 or player < 0:
    print("You choose the wrong number! You lost.")
elif player == 0 and pc_choice == 2:
    print("You win! Nice.")
elif pc_choice == 0 and player == 2:
    print("You lost! :(")
elif pc_choice > player:
    print("You lost! :(")
elif player > pc_choice:
    print("You win! Nice.")
elif pc_choice == player:
    print("DRAW!")
