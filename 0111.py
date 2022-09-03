count = int(input('Enter count: '))
sum = avg = 0
for i in range(0,count):
    number = int(input('Enter a number: '))
    sum += number

avg = float(sum) / count

print('Sum = {0}'.format(sum))
print ('avg = {0}'.format(avg))


