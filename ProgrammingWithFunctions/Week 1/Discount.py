from datetime import datetime

disc_rate = .10
sales_tax_rate = .06

subtotal = float(input('Please enter the subtotal: '))
current_date_and_time = datetime.now()

weekday = current_date_and_time.weekday()

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * disc_rate, 2)
    print(f'Discount amount: {discount:.2f}')
    subtotal -= discount

sales_tax = round(subtotal * sales_tax_rate, 2)
print(f'Sales tax amount: {sales_tax:.2f}')

total = subtotal + sales_tax
print(f'Total: {total:.2f}')