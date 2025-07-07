#def main():
#    text_list = read_list('Plants.txt')
#    print(text_list)

#def read_list(filename):
#    text_list = []
#    with open ('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Programming with functions\\Week 5\\Plants.txt') as text_file:
#        for line in text_file:
#            clean_line = line.strip()
#            text_list.append(clean_line)
#    return text_list

#if __name__ == '__main__':
#    main()
#print('-----------------------------------------')
#import csv
#def main():
#    with open('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Programming with functions\\Week 5\\Hymns.csv') as csv_file:
#        reader = csv.reader(csv_file)
#        for row_list in reader:
#            print(row_list)
#if __name__ == "__main__":
#    main()
#print('-----------------------------------------')
#import csv
#def main():
#    dentists_list = read_compound_list("dentists.csv")
#    print(dentists_list)
#def read_compound_list(filename):
#    compound_list = []
#    with open('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Programming with functions\\Week 5\\Dentists.csv') as csv_file:
#        reader = csv.reader(csv_file)
#        for row_list in reader:
#            if len(row_list) != 0:
#                compound_list.append(row_list)
#    return compound_list
#if __name__ == "__main__":
#    main()
#print('-----------------------------------------')
#import csv
#def main():
#    PHONE_INDEX = 2
#    dentists_dict = read_dictionary("Dentists.csv", PHONE_INDEX)
#    print(dentists_dict)
#def read_dictionary(filename, key_column_index):
#    dictionary = {}
#    with open('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Programming with functions\\Week 5\\Dentists.csv') as csv_file:
#        reader = csv.reader(csv_file)
#        next(reader)
#        for row_list in reader:
#            if len(row_list) != 0:
#                key = row_list[key_column_index]
#                dictionary[key] = row_list
#    return dictionary
#if __name__ == "__main__":
#    main()
#print('-----------------------------------------')
def main():
    provinces_list = read_list('Provinces.txt')
    print(provinces_list)
    provinces_list.pop(0)
    provinces_list.pop()
    for i in range(len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'
    count = provinces_list.count('Alberta')

    print()
    print(f'Alberta occurs {count} times in the modified list.')

def read_list(filename):
    text_list = []
    with open ('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Programming with functions\\Week 5\\Provinces.txt') as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list

if __name__ == '__main__':
    main()