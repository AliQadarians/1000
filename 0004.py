from math import pi , tan

length = float(input('Enter lenght of polygon: '))
number = int(input('Enter number of polygon: '))
area = (number * (length ** 2 )) / (4 * tan(pi/number))

print('Area of polygon is {0} .'.format(round(area,2)))