from cgi import print_arguments


print('y=ax+b')
print('y=2x+c')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

x = (b-c) / (3-a)
y= 3 * x + c

print('x = {0} , y = {1}'.format(x,y))