# def main():
#    students_dict = {
#        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
#        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
#        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
#        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
#        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
#        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
#    }
#    GIVEN_NAME_INDEX = 0
#    SURNAME_INDEX = 1
#    EMAIL_INDEX = 2
#    CREDITS_INDEX = 3
#    total = 0
#    for key, value in students_dict.items():
#        credits = value[CREDITS_INDEX]
#        total += credits
#    print(f"Total credits earned by all students: {total}")
#if __name__ == "__main__":
#    main()



# def main():
#    numbers_list = ["42-039-4736", "61-315-0160",
#            "10-450-1203", "75-421-2310", "07-103-5621"]
#    names_list = ["Clint Huish", "Amelia Davis",
#            "Ana Soares", "Abdul Ali", "Amelia Davis"]
#    student_dict = dict(zip(numbers_list, names_list))
#    print("Dictionary:", student_dict)
#    print()
#    keys = list(student_dict.keys())
#    values = list(student_dict.values())
#    print("Keys:", keys)
#    print()
#    print("Values:", values)
#if __name__ == "__main__":
#    main()





def main():
    students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }

#ou

# def main():
#    students_dict = {
#        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
#        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
#        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
#        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
#        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
#    }
    students_dict["81-298-9238"] = "Sama Patel"
    students_dict.pop("61-315-0160")
    length = len(students_dict)
    print(f"length: {length}")
    print(students_dict)
    print()
    id = input("Enter a student ID: ")
    if id in students_dict:
        name = students_dict[id]
        print(name)
    else:
        print("No such student")
if __name__ == "__main__":
    main()