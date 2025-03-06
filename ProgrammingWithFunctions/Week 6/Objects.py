#def main():
#    numbers = [87, 95, 72, 92, 95, 88, 84]
#    total = 0
#    for x in numbers:
#        total += x
#    average = total / len(numbers)
#    print(f"average: {average:.2f}")
    
#if __name__ == "__main__":
#    main()
#print('------------------------------------')
#def main():
#    fabrics = []
#    fabrics.append("velvet")
#    fabrics.append("denim")
#    fabrics.append("gingham")
#    fabrics.insert(0, "chiffon")
#    print(fabrics)
#    i = fabrics.index("velvet")
#    fabrics[i] = "taffeta"
#    print(fabrics)
#    fabrics.pop()
#    fabrics.remove("denim")
#    print(fabrics)
#if __name__ == "__main__":
#    main()
#print('------------------------------------')
def main():
    students = {
        '42-039-4736': "Clint Huish",
        '61-315-0160': "Amelia Davis",
        '10-450-1203': "Ana Soares",
        '75-421-2310': "Abdul Ali",
        '07-103-5621': "Amelia Davis",
        '81-298-9238': "Sama Patel"}
    
    id = input("Enter a student ID: ")
    name = students.get(id)
    if name:
        print(name)
        students.pop(id)
    else:
        print("No such student")
    print()
    for key, value in students.items():
        print(key, value)
if __name__ == "__main__":
    main()