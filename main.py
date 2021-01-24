"""
This application is a basic hangman game.
A random word is chosen from a list and length of the word is showed in blanks to the user.
A user start's the game with 4 chances to guess the word correctly by guessing the letters in the word.
If the user guessed correctly before the chances is at 0 they win else they lose,
while each wrong guess means the user loses a chance.
"""
# Add the imports
from words import words
import random

# Choose a random word from the list of words
selected_word = random.choice(words)

# For testing will be removed when the game is complete
print(f'The selected word is: {selected_word}\n')

# Creating a blank the length of the word
selected_word_length = len(selected_word)
blanks = []
for letter in range(selected_word_length):
    blanks += '_'
print(f'Guess the word: {blanks}\n')

# Add a while loop to iterate until the user guess correctly
is_game_over = False

while not is_game_over:
    # Prompt the user
    user = input('Guess a letter that exists in the word: ').lower()

    # Loop through to check if the user input exists in the selected word
    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == user:
            blanks[position] = letter
    print(blanks)

    if '_' not in blanks:
        is_game_over = True
        print(f'The word is {selected_word}, You Win')
