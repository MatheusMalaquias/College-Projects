#I added a delay to show the overall max, min and the average life expectation, max life expectation and min life expectation.
import time

highest_expectation = 0
lowest_expectation = 100.000
highest_expectation_user = 0
lowest_expectation_user = 100.000
average_year = 0
count = 0

while True:
    user_year = input ('Enter the year of interest (4 Digits): ')

    if user_year.isdigit() and len(user_year) == 4:
        user_year = int(user_year)
        break
    else:
        print("Please enter a valid 4-digits year. ")

with open ('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Introduction to Programming\\Week 6\\LifeExpectancy.csv') as data_analysis:
    next(data_analysis)
    for item in data_analysis:
        parts = item.split(',')
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        if year == user_year:
            average_year += life_expectancy
            count += 1

        if life_expectancy < lowest_expectation:
            lowest_expectation = life_expectancy
            lowest_country = country
            lowest_year = year
       
        if life_expectancy > highest_expectation:
            highest_expectation = life_expectancy
            highest_country = country
            highest_year = year

        if int(year) == user_year:
            if life_expectancy < lowest_expectation_user:
                lowest_expectation_user = life_expectancy
                lowest_country_user = country 
                    
            if life_expectancy > highest_expectation_user:
                highest_expectation_user = life_expectancy
                highest_country_user = country 

    if count > 0:
        average_expectation = average_year / count
    else:
        average_expectation = 0 

time.sleep(2)

print ()
print (f'The overall max life expectancy is: {highest_expectation} from {highest_country} in {highest_year}')
time.sleep (1)
print (f'The overall min life expectancy is: {lowest_expectation} from {lowest_country} in {lowest_year}')
time.sleep(3)
print()
print (f'For the year {user_year}: ')
time.sleep(1)

if count > 0:
    print (f'The average life expectancy across all countries was {average_expectation:.2f}')
    time.sleep(1)
    print (f'The max life expectancy was in {highest_country_user} with {highest_expectation_user}')
    time.sleep(1)
    print (f'The min life expectancy was in {lowest_country_user} with {lowest_expectation_user}')
else:
    print ('No data found for this year')
print()