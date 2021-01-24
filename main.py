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
blanks = []
for letter in selected_word:
    blanks.append('_')
print(f'Guess the word: {blanks}\n')

# Prompt the user
user = input('Guess a letter that exists in the word: ').lower()

# Loop through to check if the user input exists in the selected word
for position in range(len(selected_word)):
    letter = selected_word[position]
    if letter == user:
        blanks[position] = letter
print(blanks)
