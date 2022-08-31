number = int(input('Enter a number: '))
find = False
f1 = f2 = 1

if number <= 0:
     find = False

elif number == 1:
    find = True
else:
    for i in range(2,number+1):
        f1, f2 = f2, f1+f2
        if f2 == number:
            find = True
            break
if find == False:
    print('NO')
else:
    print('Yes')

