#author: Matheus Malaquias

#print('Please enter the following information:')

#print('What is your first name?')
#print('What is your last name?')

first = input('First name: ')
last = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job_title = input('Job Title: ')
id_number = input('Id number: ')
hair = input('Hair: ')
month = input('Month: ')
eyes = input('Eyes: ')
trainig = input('Training: ')

print('\nThe ID card is:')
print('--------------------')
print(f"{last.upper()}, {first.capitalize()}")
print(f'{job_title}')
print(f'ID: {id_number}')
print()
print(f'{email}')
print(f'{phone}')
print('--------------------')


print('\nThe ID card is:')
print('--------------------')
print(f"{last.upper()}, {first.capitalize()}")
print(f'{job_title}')
print(f'ID: {id_number}')
print()
print(f'{email}')
print(f'{phone}')
print(f"Hair: {hair}        Eyes: {eyes}")
print(f"Month: {month}    Training: {trainig}")
print('--------------------')