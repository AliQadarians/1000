from cgi import print_arguments


n1 = int(input('Enter a number: '))
temp = n1
n2 = i = 0
while temp  > 0:
    n2 = n2 * 10 + (temp % 10)
    temp //= 10 
    i += 1

if n1 == n2 :
    print('Yes')
else:
    print('NO')