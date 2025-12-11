Step 1

import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
for char in chosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")

Step 2

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display = ""
for letter in chosen_word:
    if guess == letter:
        display += guess
    else:
        display += "_"
print(display)
