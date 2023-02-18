# start, generate a random word, generate blanks, ask user to guess, if correct continue, wrong quess leads to =1 life

import random
import hangman_words
import hangman_art
# from hangman_words import word_list
chosen_word= random.choice(hangman_words.word_list)
print(hangman_art.logo)
# print(f"Pssst, the solution is {chosen_word}")
end_of_game=False
display=[]
chosen_word_length=len(chosen_word)
lives = 6
for _ in chosen_word:
    display.append('_')
while not end_of_game:
    guess=input("Guess a letter: ").lower()
    
    # for letter in chosen_word:
    #     if letter== guess:
    #         print("Right")
    #     else:
    #         print("Wrong")
    # for add in range(chosen_word_length):   
    #     display.append('_')
    if guess in display:
        print(f"You have already guessed the letter {guess}.")
    for position in range(chosen_word_length):
        letter=chosen_word[position]
        if letter== guess:
            display[position]=letter
       

    if guess not in chosen_word:
        print(f"You have already guessed {guess}, that's not in the word. You lose a life")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose")

    print(f"{' '.join(display)}")   
    if "_" not in display:
        end_of_game=True
        print("You Win")
    print(hangman_art.stages[lives])#when lives=0, stages[0] will be printed


