from re import I


while True : 
    number = int(input('Enter a number: '))
    i = 2
    sum = 1

    while i <= number / 2 :
        if number % i == 0 :
            sum += i
        i += 1

    if number == 1 :
        print('Not perfected')
    elif sum == number :
        print('Perfect')
    else:
        print('Not perfect')
    
    yes = input('Do you like continue(y/n): ')
    if yes == 'y' or yes == 'Y' :
        continue
    else:
        break
