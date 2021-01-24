"""
This application is a basic hangman game.
A random word is chosen from a list and length of the word is showed in blanks to the user.
A user start's the game with 5 chances to guess the word correctly by guessing the letters in the word.
If the user guessed correctly before the chances is at 0 they win else they lose,
while each wrong guess means the user loses a chance.
"""
# Add the imports
from words import words
from logo import chances_stage, logo
import random

# display the logo
print(logo)

# Choose a random word from the list of words
selected_word = random.choice(words)

# Instruction
print('Game Instructions: \n'
      'A random word is selected and the length of the word is shown in blanks.\n'
      'Guess the word by guessing the letters that are in it.\n'
      'You start with 5 chances to get the word correctly and win the game.\n'
      'You do not lose a chance if you repeat the correct letter you have guessed already.\n')

# Creating a blank the length of the word
selected_word_length = len(selected_word)
user_display = []
for letter in range(selected_word_length):
    user_display += '_'
    user_display_string = ' '.join(user_display)
print(f'Guess the word: {user_display_string}')

# Set the user chances
chances = 5
print(f'Chances: {chances}\n')

# Add a while loop to iterate until the user guess correctly
is_game_over = False

while not is_game_over:
    # Prompt the user
    user_guess = input('Guess a letter that exists in the word: ').lower()

    # Check if the user as guessed the letter already
    if user_guess in user_display:
        print(f'"{user_guess}" is a correct guess already.')

    # Loop through to check if the user input exists in the selected word
    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == user_guess:
            user_display[position] = letter
    user_display_string = ' '.join(user_display)
    print(f'{user_display_string}\n')

    # Remove 1 chance from the user chances, when it's 0 stop iteration.
    if user_guess not in selected_word:
        print(f'Wrong guess, "{user_guess}" does not exist in the word.')
        chances -= 1
        if chances == 0:
            is_game_over = True
            print('You have no more chances. You lose, Try again!!!')
            print(f'The correct word is {selected_word}.')
        elif chances == 1:
            print(f'You have {chances} chance remaining. Be careful!!!')
        else:
            print(f'You have {chances} chances remaining.')
        # display the user chances stage
        print(chances_stage[chances])

    # Stop iteration when there are no more blanks
    if '_' not in user_display:
        is_game_over = True
        print(f'You guessed the word "{selected_word}" correctly. You Win!!!')

        if chances > 1:
            print(f'You finished with {chances} chances remaining.')
            print(chances_stage[chances])
        else:
            print(f'You finished with {chances} chance remaining, wow that was close.')
            print(chances_stage[chances])
