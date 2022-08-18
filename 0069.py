number = int(input('Enter number: '))
n = int(input('Enter nth bit to set (1-31): '))

new = (1<<n) ^ number

print('New number is ', new)