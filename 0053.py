from socket import inet_ntoa


a = int(input('Enter a: '))
b = int(input('Enter b: '))

print('a = {0}, b = {1}'.format(a,b))
a, b = b , a

print('a = {0}, b ={1}'.format(a,b))