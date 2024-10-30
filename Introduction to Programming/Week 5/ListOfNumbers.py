numbers = []
numbers_total = 0
print('Enter a list of numbers, type 0 when finished.')
print('--------------------')
number = int(input('Enter number: '))
numbers.append(number)
while number != 0:
    number = int(input('Enter number: '))
    if number != 0:
        numbers.append(number)
for numbers_amount in numbers:
    numbers_total += numbers_amount
print('--------------------')
print(f'The sum is: {numbers_total}')
print('--------------------')
count = len(numbers)
average = numbers_total / count
print(f'The average is: {average}')
print('--------------------')
largest = -1
for number in numbers:
    if number > largest:
        largest = number
print(f'The largest number is: {largest}')
print('--------------------')
smallest_positive = 999999999999
for number in numbers:
    if number > 0 and number < smallest_positive:
        smallest_positive = number
print(f'The smallest positive number is: {smallest_positive}')
print('--------------------')
sorted_list = sorted(numbers)
print('The sorted list is:')
for number in sorted_list:
    print(number)