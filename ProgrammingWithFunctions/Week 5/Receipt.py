import csv

def read_dictionary(filename):
    products_dict = {}
    with open('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Programming with functions\\Week 5\\Products.csv') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if row:
                key = row[0]
                products_dict[key] = {'name': row[1], 'price': float(row[2])}
    return products_dict

def main():
    products_dict = read_dictionary('Products.csv')
    print(products_dict)
    print('Requested items')

    with open('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Programming with functions\\Week 5\\Request.csv') as request_file:
        request_reader = csv.reader(request_file)
        next(request_reader)
        for row in request_reader:
            if row:
                product_number = row[0]
                quantity = int(row[1])
                if product_number in products_dict:
                    product_name = products_dict[product_number]['name']
                    product_price = products_dict[product_number]['price']
                    
                    print(f'{product_name}: {quantity} @ {product_price:.2f}')

if __name__ == "__main__":
    main()