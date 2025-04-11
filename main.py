import random
from random_word import RandomWords
from hangman_art import stages, logo

r = RandomWords()

# Start
print(logo)
word = r.get_random_word()

positions = ""
word_length = len(word)
for position in range(word_length):
    positions += "_"
print("Word to guess: " + positions)

lives = 6

game_over = False
correct_letters = []

while not game_over:
    print(f"=================================YOU HAVE {lives} LIVES LEFT=================================")
    guess = input('Guess a letter: ').lower()

    display = ""

    for letter in word:
        if guess == letter:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            print(f"You've already guessed {guess}")
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"=================================THE CORRECT WORD IS {(word).upper()}! YOU LOSE=================================")
    
    if "_" not in display:
        game_over = True
        print("=================================YOU WIN!=================================")
    
    print(stages[lives])