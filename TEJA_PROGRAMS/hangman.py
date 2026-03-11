hangman = """"
                                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
"""
print(hangman)

import random as r

Words = ["apple", "banana", "orange", "mango", "grape", "pineapple", "strawberry", "blueberry", "watermelon", "papaya",
         "peach", "kiwi", "cherry", "lemon", "avocado", "carrot", "potato", "tomato", "onion", "broccoli", "spinach",
         "cucumber", "cauliflower", "garlic", "cabbage", "sweet corn"]
chosen_word = r.choice(Words)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives, display = 6, []

for i in range(len(chosen_word)):
    display += "_"

end_game = True

while end_game:

    guess = input("guess letter?").lower()
    if guess in display:
        print(f"you already guessed {guess}")

    for i in range(len(chosen_word)):
        if guess in chosen_word[i]:
            display[i] = guess

    if guess in display:
        print(f"YOU GUESSED {guess},RIGHT")

    else:
        lives -= 1
        print(f"GUESSED LETTER IS {guess} ,YOU GUESSED WRONG ,YOU LOST A LIFE")

    if lives == 0:
        print("YOU LOST THE GAME")
        end_game = False

    guessed_word = ""
    for i in display:
        guessed_word += "  "
        guessed_word += i
    print(guessed_word)

    if "_" not in display:
        end_game = False
        print("you Won")

    print(stages[lives])
