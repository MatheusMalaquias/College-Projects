# with open('course.txt') as course_file:
#     for line in course_file:
#         print(line)



# colors = 'red,green,blue,yellow'
# color_parts = colors.split(',')
#color_parts = ['red', 'green', 'blue', 'yellow']
#print(colors)
# print(color_parts)

# for color in color_parts:
#     print(color)



#Aparecer somente uma cor específica#
# second = color_parts[1]
# print(second)



# name = 'Matheus Otávio'
# #clean_name = name.strip()
# name = name.strip()
# print(f'---{name}---')
# #print(f'---{clean_name}---')



# with open('course.txt') as course_file:
#     for line in course_file:
#         #line = 'CSE 110,98.5'
#         line = line.strip()
#         parts = line.split(',')
#         #parts = ['CSE 110, 98.5']
#         name = parts[0]
#         grade = float(parts[1])
#         bonus_grade = grade + 3
#         print(f'{name} - Grade: {grade}, after bonus: {bonus_grade}')

# with open('books.txt') as book_file:
#     for line in book_file:
#         book = line.strip()
#         print(book)

# numbers = [42, 25, 18, 83, 23, 85, 38, 2]
# largest_so_far = numbers[0]
# for number in numbers:
#     if number > largest_so_far:
#         largest_so_far = number
# print(f'The largest number is: {largest_so_far}')

# shopping_cart = [['Chips', 2.99], ['Bread', 2.50], ['Milk', 3.19], ['Ice Cream', 6.99], ['Cheese', 5.99], ['Candy bar', 0.99]]
# max_price = -1
# max_product = ''
# for item in shopping_cart:
#     product_name = item[0]
#     price = item[1]
#     if price > max_price:
#         max_price = price
#         max_product = product_name
# print(f'The maximum price is: {max_price}')
# print(f'The product with the maximum price is: {max_product}')

# people = ['Stephanie 36', 'John 29', 'Emily 24', 'Gretchen 54', 'Noah 12', 'Penelope 32', 'Michael 2', 'Jacob 10']    
# youngest_age = 9999
# youngest_name = ''
# for person in people:
#     parts = person.split()
#     name = parts[0]
#     age = int(parts[1])
#     if age < youngest_age:
#         youngest_age = age
#         youngest_name = name
# print(f'The youngest person is: {youngest_name} with an age of {youngest_age}')