number = int(input('Enter your number: '))

n1 = number // 10 
n2 = number % 10
sum = n1 + n2
invers = n2 * 10 + n1

print('number = {0}\nsum = {1}\ninvers = {2}'.format(number, sum , invers))