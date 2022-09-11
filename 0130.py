str1 = input('Enter string: ')
count = 0
for i in str1:
    if i == '\n':
        break
    count += 1
print('char = {0}'.format(count))