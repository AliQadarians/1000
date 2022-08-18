number = int(input('Enter number: '))
n = int(input('Enter nth bit to set 1 (0-310): '))

newNumber = (1<<n) | number

print('New number is {}'.format(newNumber))