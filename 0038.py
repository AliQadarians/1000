import math
r = int(input('Enter r:'))

d = 2 * r
p = round(math.pi,2) * r * 2
a = round(math.pi,2) * r ** 2

print('r={0}\td={1}\tp={2}\ta={3}'.format(r,d,p,a))