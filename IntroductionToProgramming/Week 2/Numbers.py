#pi = 3.14159
#print(pi)

# first_number = input('Please enter a number ')
# second_number = input('Please enter another number ')
# print(first_number + second_number)
# print(int(first_number) + int(second_number))
# print(float(first_number) + float(second_number))

# days_in_February = 28
# print(str(days_in_February) + ' total days in February')

# number = 7
# print(f"The number is {number}")

# age = input('How old are you? ')
# print(f"On your next birthday, you will be {int(age) + int(1)}")
# print('--------------------')
# egg_cartons = input('How many egg cartons do you have? ')
# print(f"You have {int(egg_cartons) * int(12)} eggs")
# print('--------------------')
# cokkie = input('How many cookies do you have? ')
# people = input('How many people are there? ')
# print(f"Each person may have {int(cokkie) / int(people)} cookies")
# print('--------------------')

#O :.(numero)f irá mostrar quantas casas decimais eu quero mostrar
# cars = 3
# people = 8
# people_per_car = people / cars
# print(f"There are {people_per_car:.3f} people in each car")

# distance = 9 * 1205 * 18
# print(f"The distance is: {distance:.6e} meters")

# big_number = 123456789
# print(f"The number is: {big_number}")
# print(f"The number is: {big_number:,}")
# print(f"The number is: {big_number:_}")

# weight = 1.65
# lower = math.floor(weight)
# print(lower)

# higher = math.ceil(weight)
# print(higher)

# print('--------------------')
# fahrenheit = input('What is the temperature in Fahrenheit? ')
# print(f"The temperature in Celsius is {(int(fahrenheit) - int(32)) * (5 / 9):.1f} degress")
# print('--------------------')

print('--------------------')
square = float(input('What is the length of a side of the square? '))
print(f"The area of the square is: {float(square) ** 2:.2f}")
rectangle_length = float(input('What is the length of the rectangle? '))
rectangle_width = float(input('What is the width of the rectangle? '))
rectangle_area = (input(f"The area of the rectangle is: {float(rectangle_length) * float(rectangle_width):.2f}"))
circle_radius = float(input('What is the radius of the circle? '))
print(f"The area of the circle is: {3.14 * (float(circle_radius) ** 2):.2f}")
print('--------------------')