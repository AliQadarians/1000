def fac(i):
    p = 1
    if i == 1:
        return 1
    elif i > 1:
        for i in range(1,i+1):
            p *= i 
    return p

n = int(input('Enter n: '))
sum = 0
sig = 1
for i in range(1,n+1):
    c = fac(i)
    sum += (sig * i/c)
    print('{0}/{1}'.format(i,c), end=' ')
    if i != n:
        if sig == 1:
            print('-',end=' ')
        elif sig == -1:
            print('+',end=' ')
    sig *= -1
print('= {0}'.format(sum))
