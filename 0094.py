s = input('Enter a string: ')
sound = 'aAeEiIoOuU'
count = 0
for i in s:
    if i in sound:
        count += 1
    
print('count = {0}'.format(count))
