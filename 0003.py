import math
radius = float(input('Enter radius of sphere :'))
volum = (4 / 3) * math.pi * (radius ** 3)
area = 4 * math.pi * (radius ** 2)
print('Volum of sphere is {0} , and area is {1} .'.format(round(volum, 2), round(area, 2)))  