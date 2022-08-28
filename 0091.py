print('m ^ n ')
m = int(input('Enter m: '))
n = int(input('Enter n: '))

temp = m
sum = 0
for i in range(1,n):
    sum = 0
    for j in range(1,m+1):
        sum += temp
    temp = sum

print('{0} ^ {1} = {2} '.format(m,n,temp))
exit(0)