import random

word_list = ["lemon", "strawberry", "bird", "brasil"]
random_word = random.choice(word_list)
letters_list = len(list(random_word))

underline_list = []
for letter in random_word:
    underline_list.append("_")

lives = 7
right_guesses = 0
counting_end = 0
guessed_letters = []
chosen_letters_list = []

while lives != counting_end and right_guesses != letters_list:
    print(f"The word is:\n{underline_list}")
    guess = input("Guess a letter: ").lower()
    chosen_letters_list.insert(0, guess)
    print(f"Letters already chosen:\n{chosen_letters_list}")

    code_running = 0
    checking_list = 0

    for item in guessed_letters:
        if guess == guessed_letters[checking_list]:
            guessed_letters.remove(guess)
            right_guesses -= 1
            print("You already tried this letter, Please, Try another!")
        checking_list += 1

    for letter in random_word:
        if guess == random_word[code_running]:
            right_guesses += 1
            underline_list[code_running] = guess
            guessed_letters.append(guess)
            counting_end -= 1
        code_running += 1
    counting_end += 1

    if counting_end == 7:
        print("YOU LOSE!")
    if right_guesses == letters_list:
        print("YOU WIN!")

print(underline_list)
print("\nThe word was:")
print(random_word)