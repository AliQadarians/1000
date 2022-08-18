number1 = int(input('Enter number one: '))
number2 = int(input('Enter number two: '))

number1 = number1 ^ number2
number2 = number2 ^ number1
number1 = number1 ^ number2

print('number one is ', number1)
print('number two is ', number2)