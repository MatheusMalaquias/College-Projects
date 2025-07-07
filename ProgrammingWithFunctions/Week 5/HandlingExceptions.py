#def main():
#  try:
#    text = input("Please enter a number: ")
#    integer = round(text)
#    print(integer)
#  except TypeError as type_err:
#    print(type_err)
#if __name__ == "__main__":
#  main()
#print('-----------------------------------------')
#def main():
#  try:
#    number = float(input("Please enter a number: "))
#    print(number)
#  except ValueError as val_err:
#    print(val_err)
#if __name__ == "__main__":
#  main()
#print('-----------------------------------------')
#def main():
#  try:
#    players = int(input("Enter the number of players: "))
#    teams = int(input("Enter the number of teams: "))
#    players_per_team = players / teams
#    print(f"Each team should have {players_per_team} players")
#  except ZeroDivisionError as zero_div_err:
#    print(zero_div_err)
#if __name__ == "__main__":
#  main()
#print('-----------------------------------------')
#def main():
#  try:
#    surnames = ["Smith", "Lopez", "Marsh"]
#    print(surnames[3])
#  except IndexError as index_err:
#    print(index_err)
#if __name__ == "__main__":
#  main()
#print('-----------------------------------------')
#def main():
#  try:
#    students = {
#    '42-039-4736': 'Clint Huish',
#    '61-315-0160': 'Amelia Davi',
#    '10-450-1203': 'Ana Soares',
#    '75-421-2310': 'Abdul Ali',
#    '07-103-5621': 'Amelia Davis'}

#    id = input('Enter a student ID: ')
#    if id in students:
#      name = students[id]
#      print(name)
#    else:
#      print('No such student')

#  except KeyError as key_err:
#    print(type(key_err).__name__, key_err)
#if __name__ == '__main__':
#  main()
#print('-----------------------------------------')
def main():
  try:
    sandwiches = int(input("Number of sandwiches made today: "))
    employees = int(input("Number of employees who worked today: "))
    sands_per_emp = sandwiches / employees
    print(f"{sands_per_emp:.1f} sandwiches per employee")
  except ValueError as val_err:
    print(f"Error: {val_err}")
    print("You entered text that is not an integer. Please")
    print("run the program again and enter an integer.")
  except ZeroDivisionError as zero_div_err:
    print(f"Error: {zero_div_err}")
    print("You entered 0 for the number of employees.")
    print("Please run the program again and enter an integer")
    print("larger than 0 for the number of employees.")
if __name__ == "__main__":
  main()