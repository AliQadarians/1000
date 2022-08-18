number = int(input('Enter number: '))
n = int(input('Enter nth bit for check(0-31): '))

bitstatus = (number>>n) & 1

print('nth bit is ',bitstatus)