y1 = float(input('Enter price for first year: '))
y2 = float(input('Enter price for second year:'))
t = (y2 - y1) / y1
y3 = y1 + (y2 * t)
print('t =% {0}\n price for next year {1}'.format(t,y3))
