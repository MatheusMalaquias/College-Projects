import csv
from datetime import datetime

def read_products():
    products_dict = {}
    try:
        with open('c:/Users/NOTEBOOK/Desktop/BYU-I/Intro to Python Development/Programming with functions/Week 5/Products.csv') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                if row:
                    key = row[0]
                    products_dict[key] = {'name': row[1], 'price': float(row[2])}
    except FileNotFoundError:
        print("Error: Product file not found.")
    except PermissionError:
        print("Error: Permission denied to read the product file.")
    return products_dict

def read_request():
    request = []
    try:
        with open('c:/Users/NOTEBOOK/Desktop/BYU-I/Intro to Python Development/Programming with functions/Week 5/Request.csv') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                if row:
                    request.append(row[0])
    except FileNotFoundError:
        print("Error: Request file not found.")
    except PermissionError:
        print("Error: Permission denied to read the request file.")
    return request

def print_recept(products, request):
    try:
        print("Malaquias's Store")
        print("-" * 30)

        total_itens = 0
        subtotal = 0.0

        for produto_id in request:
            if produto_id in products:
                product = products[produto_id]
                print(f"Item: {product['name']} - Price: R$ {product['price']:.2f}")
                total_itens += 1
                subtotal += product['price']
            else:
                raise KeyError(f"Product ID {produto_id} not found.")

        print("-" * 30)
        print(f"Total number of items: {total_itens}")
        print(f"Subtotal: R$ {subtotal:.2f}")

        tax_rate = 0.06
        tax = subtotal * tax_rate
        total_due = subtotal + tax

        print(f"Sales tax (6%): R$ {tax:.2f}")
        print(f"Total due: R$ {total_due:.2f}")

        print("Thank you for your purchase!")
        print(f"Data and time: {datetime.now().strftime('%A %b %d - %H:%M:%S - %Y')}")

    except KeyError as e:
        print(f"Error: {e}")

def main():
    products = read_products()
    request = read_request()
    print_recept(products, request)

if __name__ == "__main__":
    main()