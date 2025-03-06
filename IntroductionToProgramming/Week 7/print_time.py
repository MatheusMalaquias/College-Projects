# import datetime

# first_name = 'Matheus'
# print('task completed')
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#     print(x)
# print('task completed')
# print(datetime.datetime.now())
# print()

    # /\ (completo) e \/(simplificado) são a mesma coisa

# def print_time():
#     print('task completed')
#     print(datetime.datetime.now())
#     print()

# first_name = 'Matheus'
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()

    # /\ (simplificado) e \/(mais simplificado) são a mesma coisa

from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Matheus'
print_time('printed first name')

for x in range(0,10):
    print(x)
print_time('completed for loop')