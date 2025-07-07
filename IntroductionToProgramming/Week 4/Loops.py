#tip = float(input("What is the tip anount? "))

#while tip < 0:
#     print("Sorry, the tip cannot be negative")
#     tip = float(input("What is the tip anount? "))
 
#print(f"You have tipped an anount of ${tip:.2f}")

#number = 0
#while number < 10:
#    number = int(input('What is the number? '))
#print('Finished with the loop')


#number = int(input('What is the number? '))
#while number <= 5:
#    print(f'The number is: {number}')
#    number = number + 1
#print('Finished with the loop')

#number = int(input('Please type a positive number: '))
#while number < 0:
#    print('Sorry, that is a negative number. Please try again.')
#    number = int(input('Please type a positive number: '))
#print(f'The number is: {number}')
#print('--------------------')
#answer = input('May I have a piece of candy? ')
#while answer != "yes":
#    answer = input('May I have a piece of candy? ')
#print('Thank you!')

#('--------------------') #É a mesma coisa
#1
#people = ['Matheus', 'Malaquias']
#for name in people:
#    print(name)
#2
#index = 0
#while index < len(people):
#    print(people[index])
#    index = index + 1
#('--------------------') #É a mesma coisa

#items = ['car', 'pen', 'house', 'dog']
#for items in items:
#    print(f"The item is: {items}")

#numbers = range(10)
#for numbers in range(10):
#    print(numbers)

#i = range(100, 200)
#for i in range(100, 200):
#    print(i)

#i = range(100, 200, 10)
#for i in range(100, 200, 10):
#    print(i)

#numbers = range(10)
#for numbers in range(10):
#    print(numbers)
#    for j in range(10, 13):
#        print(f"--{j}")
#('------------------------------------------------------')
#colors = ['red', 'blue', 'green', 'yellow']
#numbers = range(1, 9)
#par_numbers = range(2, 21, 2)
#for colors in colors:
#    print(colors)
#for numbers in numbers:
#    print(numbers)
#for par_numbers in range(2, 21, 2):
#    print(par_numbers)

#first_name = 'Matheus'
#for letter in first_name:
#   print(f'The letter is: {letter}')
#print()
#first_name = 'Matheus'
#fouth_letter = first_name[3]
#print(f'The letter is: {fouth_letter}')
#print()
#word = 'Matheus'
#number_of_letters = 7
#for index in range(number_of_letters):
#    letter = word[index]
#    print(f'index: {index} Letter: {letter}')

#my_name = input('What is your name? ')
#letter_count = len(my_name)
#print(f'Your name has {letter_count} letters')

#word = 'computer'
#number_of_letters = len(word)
#for index in range(number_of_letters):
#    letter = word[index]
#    print(f'index: {index} Letter: {letter}')
#('------------------------------------------------------')
#Step 1
word = 'lavar roupa'
for letter in word:
    print(letter, end="")
print()

#Step 2
favorite_letter = input('What is your favorite letter? ')
for letter in word:
    if letter.lower() ==  favorite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
#Step 3
print()
for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()