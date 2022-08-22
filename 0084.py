this_year = int(input('Enter this year: '))
breath_year = int(input('Enter breaht year: '))

age = this_year - breath_year
mounth = age * 12
day = mounth * 30
houre = day * 24
minute = houre * 60
second = minute  * 60

print('age = {} year'.format(age))
print('age = {} mounth'.format(mounth))
print('age = {} day'.format(day))
print('age = {} houre'.format(houre))
print('age = {} minute'.format(minute))
print('age = {} second'.format(second))