a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

max = max(a,b,c)
min = min(a,b,c)
medel = (a+b+c) - (max + min)

print('{0} < {1} < {2}'.format(min,medel,max))