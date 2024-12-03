def main():
    try:
        filename = input("Enter the name of text file: ")
        text_lines = read_list(filename)
        linenum = int(input("Enter a line number: "))
        line = text_lines[linenum - 1]
        print()
        print(line)

    except FileNotFoundError as not_found_err:
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {filename} doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")

    except PermissionError as perm_err:
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {filename}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")

    except ValueError as val_err:
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for" \
                " the line number.")

    except IndexError as index_err:
        print()
        print(type(index_err).__name__, index_err, sep=": ")
        length = len(text_lines)
        if linenum < 0:
            print(f"{linenum} is a negative integer.")
        else:
            print(f"{linenum} is greater than the number" \
                    f" of lines in {filename}.")
            print(f"There are only {length} lines in {filename}.")
        print(f"Run the program again and enter a line number" \
                f" between 1 and {length}.")

    except Exception as excep:
        print()
        print(type(excep).__name__, excep, sep=": ")


def read_list(filename):
    text_lines = []
    with open('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Programming with functions\\Week 5\\Accidents.csv') as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_lines.append(clean_line)
    return text_lines

if __name__ == "__main__":
    main()