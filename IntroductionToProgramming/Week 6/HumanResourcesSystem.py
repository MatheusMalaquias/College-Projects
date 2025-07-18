with open('c:\\Users\\NOTEBOOK\\Desktop\\BYU-I\\Intro to Python Development\\Introduction to Programming\\Week 6\\HrSystem.txt') as informations_file:
    for line in informations_file:
        parts = line.split()
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])
        pay_amount = salary / 24
        if job_title.lower() == 'engineer':
            pay_amount += 1000
        print(f'{name} (ID: {id_number}), {job_title} - ${pay_amount:.2f}')