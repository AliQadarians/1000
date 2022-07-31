x = int(input('y=31x-17x+5\nEnter x: '))

m = (x << 5) - x
n = (x << 4) + x
y = m - n + 5

print('y=31*{0}-17{0}+5={1}'.format(x,y))