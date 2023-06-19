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

error = '''
                                                         
                                                         
                                                         
                                                         
 ,adPPYba, 8b,dPPYba, 8b,dPPYba,  ,adPPYba,  8b,dPPYba,  
a8P_____88 88P'   "Y8 88P'   "Y8 a8"     "8a 88P'   "Y8  
8PP""""""" 88         88         8b       d8 88          
"8b,   ,aa 88         88         "8a,   ,a8" 88          
 `"Ybbd8"' 88         88          `"YbbdP"'  88          
                                                         
                                                         
'''

print("Hi!\nWelcome to the Rock, Papers and Scizors game!\nYou are going to be facing the Bot.\n")
print("Type: 1 or rock.\nTo choose Rock\n\nType: 2 or paper.\nTo choose Paper\n\nType: 3 or scissor.\nTo choose Scissor\n\n\n")
choice = input("Type here: ")

choice.lower()
number_choice_lowercase = int(choice)
if choice == 'rock':
    number_choice_lowercas = 1
elif choice == 'paper':
    number_choice_lowercase = 2
elif choice == 'scissor' or choice == 'scissors':
    number_choice_lowercase = 3


hands = [rock, paper, scissors]

npc_choice = random.randint(1, 3)

if choice == '1' or choice == 'rock':
    print("You choose Rock!")
    print(hands[number_choice_lowercase - 1])
elif choice == '2' or choice == 'paper':
    print("You choose Paper!")
    print(hands[number_choice_lowercase - 1])
elif choice == '3' or choice == 'scissor' or choice == 'scissors':
    print("You choose Scissor!")
    print(hands[number_choice_lowercase - 1])
else:
    print("You choose nothing!")
    print(error)

if npc_choice == 1:
    print("The Bot choose Rock!")
    print(hands[npc_choice-1])
elif npc_choice == 2:
    print("The Bot choose Paper!")
    print(hands[npc_choice-1])
elif npc_choice == 3:
    print("The Bot choose Scissor!")
    print(hands[npc_choice-1])


if number_choice_lowercase > 3 or number_choice_lowercase <= 0:
    print("\nYou've typed a invalid number!\nYou lose!")
elif number_choice_lowercase == npc_choice:
    print("\nIt's a Draw!")
elif number_choice_lowercase < npc_choice and number_choice_lowercase + 1 != npc_choice:
    print("\nYou Won!")
elif number_choice_lowercase < npc_choice and number_choice_lowercase + 1 == npc_choice:
    print("\nYou Lose!")
elif number_choice_lowercase > npc_choice and number_choice_lowercase - 1 == npc_choice :
    print("\nYou Won!")
elif number_choice_lowercase > npc_choice and number_choice_lowercase - 1 != npc_choice:
    print("\nYou Lose!")
    