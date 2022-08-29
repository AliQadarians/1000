number1 = int(input('Enter a positive number:'))
number2 = int(input('Enter a positive number: '))
counter = 0

if number1 < number2:
    temp = number1
    number1 = number2
    number2 = temp

temp = number1
    
while temp >= number2:
    temp = temp - number2
    counter += 1

print('{0} / {1} = {2}'.format(number1,number2,counter))