n = int(input('Enter n: '))
sum = 0
for i in range(1,n+1):
    sum += i
    print('{0}'.format(i),end=' ')
    if i != n:
        print('+',end=' ')

print(' = {0}'.format(sum))
