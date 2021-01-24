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
print(f'The selected word is: {selected_word}')

