a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if (a != 0) and (b != 0) and (c != 0):
    if a+b >= c:
        if a+c >= b:
            if c+b >= a:
                print('Yes')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')   
else:
    print('numbers has zero')