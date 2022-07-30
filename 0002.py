import math

heigh = float(input('Enter heigh of cylinder : '))
radius = float(input('Enter radius of cylinder :'))
volum = heigh * math.pi * radius ** 2
area = 2 * math.pi * radius * heigh + 2 * math.pi * radius ** 2
print('Voum is {0} and area is {1} .'.format(round(volum,1),round(area,1)))