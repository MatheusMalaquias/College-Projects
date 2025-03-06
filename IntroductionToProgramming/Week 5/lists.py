#clients = []

# clients.append('Mary')
# clients.append('John')
# clients.append('Josh')
# clients.append('Max')
# print(clients)
#ou
# clients.append('Mary')
# clients.append('John')
# clients.append('Josh')
# clients.append('Max')
# for client in clients:
#     print(client)

# print('----------')
# new_client = input('What is the name of a client? ')
# clients.append(new_client)
# for client in clients:
#     print(client)
# print('----------')
# new_client = ''
# while new_client != 'quit':
#     new_client = input('What is the name of a client? ')
#     clients.append(new_client)
# for client in clients:
#     print(client)





#NUMERIC LIST#

# friends = ['Nephi', 'Lehi', 'Matthew', 'Sariah']
# tips = [12.25, 13.95, 8.50, 32.50]

# running_total = 0

# for tip_amount in tips:
    #running_total = running_total + tip_amount
    #é a mesma coisa
#     running_total += tip_amount
# print(f'The total is: {running_total:.2f}')







# friends = []
# new_friend = input('Type the name of a friend: ')
# friends.append(new_friend)
# while new_friend != 'end':
#     new_friend = input('Type the name of a friend: ')
#     if new_friend != 'end':
#         friends.append(new_friend)
# print('Your friends are:')
# for friend in friends:
#     print(friend)





# names = ['Matheus', 'Solange']
# numbers = ['(32)99139-6384', '(32)98412-8369']

# for i in range(len(names)):
#     name = names[i]
#     number = numbers[i]
#     print(f'{name} - {number}')





# items = []
# print('Please enter the items of the shopping list (type: quit to finish):')
# print('--------------------')
# item = input('Item: ' )
# items.append(item)
# while item != 'quit':
#     item = input('Item: ' )
#     if item != 'quit':
#         items.append(item)
# print('--------------------')
# print('The shopping list is:')
# for item in items:
#     print(item)
# print('--------------------')
# print('The shopping list with index is:')
# for i in range(len(items)):
#     item = items[i]
#     print(f'{i}. {item}')
# print('--------------------')
# index = int(input('Which item would you like to change? '))
# new_item = input('What is the new item? ')
# items[index] = new_item
# print('--------------------')
# print('The shopping list with indexes is:')
# for i in range(len(items)):
#     item = items[i]
#     print(f'{i}. {item}')