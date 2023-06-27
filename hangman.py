import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

word_list = ["lemon", "strawberry", "bird", "brasil"]
random_word = random.choice(word_list)
letters_list = len(list(random_word))

underline_list = []
for letter in random_word:
    underline_list.append("_")

lives = 6
right_guesses = 0
end_game = 0
guessed_letters = []
chosen_letters_list = []

while lives != end_game and right_guesses <= letters_list:
    print(stages[end_game])
    print(f"The word is:\n{underline_list}")
    guess = input("Guess a letter: ").lower().strip()
    if guess == random_word:
        right_guesses = 7
    chosen_letters_list.append(guess)
    print(f"Letters already chosen:\n{chosen_letters_list}")

    code_running = 0
    checking_list = 0
    checking_chosen_list = 0
    repeated_letter = 0

    for item in guessed_letters:
        if guess == guessed_letters[checking_list]:
            guessed_letters.remove(guess)
            right_guesses -= 1
            print("You already tried this letter, Please, Try another!")
        checking_list += 1

    for item in chosen_letters_list:
        if repeated_letter >= 1:
            if guess == chosen_letters_list[checking_chosen_list]:
                chosen_letters_list.remove(guess)
                checking_chosen_list -= 1
                repeated_letter -= 1
        if guess == chosen_letters_list[checking_chosen_list]:
            repeated_letter = 1
        checking_chosen_list += 1

    for letter in random_word:
        if guess == random_word[code_running]:
            right_guesses += 1
            underline_list[code_running] = guess
            guessed_letters.append(guess)
        code_running += 1

    end_game = len(chosen_letters_list) - len(guessed_letters)

    if end_game == lives:
        print("\n\nYOU LOSE!\nThe word was:", random_word.capitalize(), "\nYour tries were:", underline_list)
    if right_guesses >= letters_list:
        print(f"\n\nYOU WIN!\n{underline_list}\nThe word was: {random_word.capitalize()}")