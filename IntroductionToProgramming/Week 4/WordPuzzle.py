#I added a delay to appear the hints and the guess
import random 
import time

tentativas = 1

random_list = ('computer', 'blue', 'flower', 'picture', 'know', 'tower', 'television', 'faith', 'four')
random_word = random.choice(random_list)

list_random_word = list(random_word)
initial_hint = "_" * len(list_random_word)
len_random_word = len(list_random_word)

#Start
print('Welcome to the word guessing game!!')
time.sleep(3)

print("Your hint is:", initial_hint)
guess = input('What is your guess? ')
time.sleep(3)
while guess.lower() != random_word:
    while len(guess) != len(random_word):
        time.sleep(2)
        print('Sorry, the guess must have the same number of letters as the secret word.')
        time.sleep(3)
        print("Your hint is:", initial_hint)
        guess = input('What is your guess? ')
        tentativas = tentativas + 1

    count = 0

    for i in range(len_random_word):
        letter_guess = guess[i]
        letter_word = list_random_word[i]
        lower_guess = letter_guess.lower()
        lower_word = letter_word.lower()

        if lower_guess == lower_word:
            if count == 0:
                time.sleep(3)
                print(f"Your hint is: {lower_guess.capitalize()}", end="")
                count = 1
            else:
                time.sleep(3)
                print(f" {lower_guess.capitalize()}", end="")
        elif lower_guess in list_random_word:
            if count == 0:
                time.sleep(3)
                print(f"Your hint is: {lower_guess.lower()}", end="")
                count = 1
            else:
                time.sleep(3)
                print(f" {lower_guess.lower()}", end="")
        else:
            if count == 0:
                time.sleep(3)
                print("Your hint is: _", end="")
                count = 1
            else:
                time.sleep(3)
                print("_", end="")


    print()
    time.sleep(3)
    guess = input('What is your guess? ')
    tentativas += 1

time.sleep(3)
print(f"Congratulations! You guessed it! It took you {tentativas} guesses.")