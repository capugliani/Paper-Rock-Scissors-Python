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
running = 1
user_score = 0
npc_score = 0

print("Hi!\nWelcome to the Rock, Papers and Scizors game!\nYou are facing the Bot.\n")
while running == 1:
    print("Type: 1 or 'rock' to choose Rock\nType: 2 or 'paper' to choose Paper\nType: 3 or 'scissor' to choose Scissor\nOr type any other number or letter to exit!\n")
    choice = input("Type here: ")

    choice.lower()

    if choice == 'rock':
        number_choice_lowercase = 1
    elif choice == 'paper':
        number_choice_lowercase = 2
    elif choice == 'scissor' or choice == 'scissors':
        number_choice_lowercase = 3
    else:
        number_choice_lowercase = 0

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
        running = 0

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
        print("\nYou've typed invalid characters!\nYou lose!")
        npc_score += 1
    elif number_choice_lowercase == npc_choice:
        print("\nIt's a Draw!")
    elif number_choice_lowercase < npc_choice and number_choice_lowercase + 1 != npc_choice:
        print("\nYou Won!")
        user_score += 1
    elif number_choice_lowercase < npc_choice and number_choice_lowercase + 1 == npc_choice:
        print("\nYou Lose!")
        npc_score += 1
    elif number_choice_lowercase > npc_choice and number_choice_lowercase - 1 == npc_choice :
        print("\nYou Won!")
        user_score += 1
    elif number_choice_lowercase > npc_choice and number_choice_lowercase - 1 != npc_choice:
        print("\nYou Lose!")
        npc_score += 1

    print(f"\nYour Score: {user_score}\nThe Bot score:{npc_score}\n\n")

    if number_choice_lowercase == 1 or number_choice_lowercase == 2 or number_choice_lowercase == 3:
        running = 1
    else:
        running = 0
    