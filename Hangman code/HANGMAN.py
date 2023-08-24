import random

import Hangman_words


chosen_word = random.choice(Hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from Hangman_art import logo
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You have already guessed the letter\n{guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
      print(f"You guessed {guess}, That's not in the letter,You lose a life")
        
      lives -= 1
    if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from Hangman_art import stages
    print(stages[lives])


