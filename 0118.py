n = int(input('Enter n: '))
sig = 1
sum = 0
for i in range(1,n+1):
    sum += (sig * i)
    print('{0}'.format(i),end=' ')
    if i != n:
        if sig == 1:
            print('-',end=' ')
        if sig == -1:
            print('+',end=' ')
    sig *= -1

        
print('= {0}'.format(sum))