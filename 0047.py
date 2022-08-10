M_PER_MIlle = 1609.25
M_PER_FOOT = 0.30480
mille = float(input('Etner number of milles: '))
foot = float(input('Enter number of foot: '))

meter= float ( mille * M_PER_MIlle + foot * M_PER_FOOT )
kilometer = float (meter / 1000)

print('{0} milles and {1} foot = {2} meter = {3} kilometer'.format(mille,foot,meter,kilometer))
