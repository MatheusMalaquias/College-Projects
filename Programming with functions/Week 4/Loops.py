#for name in ['Christopher', 'Susan']:
#    print(name)

#for index in range(0, 2):
#    print(index)

#names = ['Christopher', 'Susan']
#index = 0
#while index < len(names):
#    print(names[index])
#    index = index + 1


# def main():
#    colors = ["red", "orange", "yellow", "green", "blue"]
#    for color in colors:
#        print(color)
#if __name__ == "__main__":
#    main()

# def main():
#    for i in range(10):
#        print(i)
#    print()
#    for i in range(5, 10):
#        print(i)
#    print()
#    for i in range(0, 10, 2):
#        print(i)
#    print()
#    for i in range(100, 69, -3):
#        print(i)
#if __name__ == "__main__":
#    main()

# def main():
#    colors = ["red", "orange", "yellow", "green", "blue"]
#    for color in colors:
#        print(color)
#    print()
#    for i in range(len(colors)):
#        color = colors[i]
#        print(color)
#if __name__ == "__main__":
#    main()

# def main():
#    sum = 0
#    for i in range(10):
#        number = float(input("Please enter a number: "))
#        if number == 0:
#            break
#        sum += number
#    print(f"sum: {sum}")
#if __name__ == "__main__":
#    main()

# def main():
#    list1 = ["red", "orange", "yellow", "green", "blue"]
#    list2 = ["red", "orange", "green", "green", "blue"]
#    index = compare_lists(list1, list2)
#    if index == -1:
#        print("The contents of list1 and list2 are equal")
#    else:
#        print(f"list1 and list2 differ at index {index}")
# def compare_lists(list1, list2):
#    length1 = len(list1)
#    length2 = len(list2)
#    limit = min(length1, length2)
#    i = 0
#    while i < limit:
#        element1 = list1[i]
#        element2 = list2[i]
#        if element1 != element2:
#            break
#        i += 1
#    if length1 == length2 == i:
#        i = -1
#    return i
#if __name__ == "__main__":
#    main()

def main():
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3
    apple_tree_data = [
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]
    total_fruit_amount = 0
    for inner_list in apple_tree_data:
        fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]
        print(fruit_amount)
        total_fruit_amount += fruit_amount
    print(f"Total fruit amount: {total_fruit_amount:.1f}")
if __name__ == "__main__":
    main()