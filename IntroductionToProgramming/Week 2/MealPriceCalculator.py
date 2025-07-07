#I added a delay to 3 seconds to show the results to subtotal, salex tax, total and change
import time

print('--------------------')
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input('How many children are there? '))
adult = int(input('How many adults are there? '))
time.sleep (3)
subtotal = (child_meal * children) + (adult_meal * adult)
print('--------------------')
time.sleep (3)
print(f"Subtotal: ${(subtotal):.2f}")
print('--------------------')
salex_tax_rate = float(input('What is the sales tax rate? '))
time.sleep(3)
tex = (salex_tax_rate / 100) * subtotal
print(f'Salex tax: ${(tex):.2f}')
time.sleep(3)
total = (tex + subtotal)
print(f'Total: ${(total):.2f}')

print('--------------------')
payment_amount = float(input('What is the payment amount? '))
time.sleep(3)
change = ((payment_amount) - (total))
print(f'Change: ${(change):.2f}')