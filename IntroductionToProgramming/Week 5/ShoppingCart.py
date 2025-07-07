#I added a delay to appear the options that the people can choose and to appear the results when you choose the option.
import time

items = []
prices = []
action = ''
price_total = 0
items_count = len(items)
print('Welcome to the Shopping Cart Program!')
print('--------------------')
time.sleep(3)
print('Please select one of the following:')
print('1. Add item')
print('2. View cart')
print('3. Remove item')
print('4. Compute total')
print('5. Quit')
action = input('Please enter an action: ')
time.sleep(3)
while action == '1':
    new_item = input('What item would you like to add? ')
    items.append(new_item)
    price = float(input(f'What is the price of {new_item}? '))
    time.sleep(3)
    prices.append(price)
    print(f'{new_item} has been added to the cart.')
    print('--------------------')
    time.sleep(3)
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = input('Please enter an action: ')
time.sleep(3)
if action == '2':
    print('The contents of the shopping cart are:')
    time.sleep(3)
    for i in range(len(items)):
        print(f'{i + 1}. {items[i]} - ${prices[i]:.2f}')

print('--------------------')
time.sleep(3)
print('Please select one of the following:')
print('1. Add item')
print('2. View cart')
print('3. Remove item')
print('4. Compute total')
print('5. Quit')
action = input('Please enter an action: ')

time.sleep(3)
if action == '3':
    remove = int(input('Which item would you like to remove? '))
    items.pop(remove - 1)
    prices.pop(remove - 1)
    time.sleep(3)
    print('Item removed.')
    items_count -= 1
    time.sleep(3)
    print('--------------------')
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = input('Please enter an action: ')
    time.sleep(3)
    if action == '2':
        print('The contents of the shopping cart are:')
        time.sleep(3)
    for i in range(len(items)):
        print(f'{i + 1}. {items[i]} - ${prices[i]:.2f}')

print('--------------------')
time.sleep(3)
print('Please select one of the following:')
print('1. Add item')
print('2. View cart')
print('3. Remove item')
print('4. Compute total')
print('5. Quit')
action = input('Please enter an action: ')

time.sleep(3)
if action == '4':
    price_total = sum(prices)
    time.sleep(3)
    print(f'The total price of the items in the shopping cart is ${price_total:.2f}')

print('--------------------')
time.sleep(3)
print('Please select one of the following:')
print('1. Add item')
print('2. View cart')
print('3. Remove item')
print('4. Compute total')
print('5. Quit')
action = input('Please enter an action: ')

print('--------------------')
time.sleep(3)
if action == '5':
    time.sleep(3)
    print('Thank you. Goodbye.')