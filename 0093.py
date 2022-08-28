number = int(input('Enter count: '))
count_Of_Meal = count_Of_Femile = salary_Of_meal = salary_Of_Femile = 0

for i in range(1,number+1):
    id = int(input('Enter ID: '))
    date = int(input('Enter date: '))
    gender = int(input('Enter gender(0/1): '))
    bace = int(input('Enter bace(1-9):'))
    salary = float(input('Enter salary: '))
    if gender == 0:
        count_Of_Femile += 1
        salary_Of_Femile += salary
        continue
    elif gender == 1:
        count_Of_Meal += 1
        salary_Of_meal += salary
        continue

print('men = {0}\tmean = {1}'.format(count_Of_Meal,salary_Of_meal/count_Of_Meal))
print('women = {0}\tmean = {1}'.format(count_Of_Femile,salary_Of_Femile/count_Of_Femile))

    
