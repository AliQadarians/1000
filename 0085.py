a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

if a < b:
    temp = a
    a = b
    b = temp
if a < c: 
    temp = a
    a = c
    c = temp
if b < c:
    temp = b
    b = c
    c = temp

print('{} > {} > {} '.format(a,b,c))
exit(0)
    
