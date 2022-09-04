n = int(input('Enter n: '))
sum = 0
sig = -1
for i in range(1,n+1):
    if sig == 1:
        print('+',end=' ')
    elif sig == -1:
        print('-',end=' ')
    sum += (sig * i)
    print('{0}'.format(i),end=' ')
    sig *= -1 
    
print('= {0}'.format(sum))