import random

number = random.randint(1, 5)
guess = int(input('What is your guess? '))
if guess > number:
    print('Lower')
    guess = int(input('What is your guess? '))
elif guess < number:
    print('Higher')
    guess = int(input('What is your guess? '))
elif guess == number:
    print('You guessed it!')

question = input('Would you like to play again (yes/no) ')
keep_playing = 'yes'
while question == 'yes':
    number = random.randint(1, 5)
guess_count = 0
guess = -1
while guess != number:
    guess = int(input('What is your guess? '))
    guess_count = guess_count + 1
    if guess < number:
        print('Higher')
    elif guess > number:
        print('Lower')
    elif guess == number:
        print('You guessed it!')
print(f'It took you {guess_count} guesses')
question = input('Would you like to play again (yes/no)? ')
print('Thank you for playing. Goodbye!')