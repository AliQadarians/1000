count = int(input('Enter count: '))
f1 = f2 = 1

if count <= 0:
    print('smaller than 1')
elif count == 1:
    print(f1)
elif count == 2: 
    print(f1)
    print(f2)
else:
    i = 0
    print(f1)
    print(f2)
    while i < count - 2 :
        f1 , f2 = f2 , f1 + f2
        print(f2)
        i += 1

exit(0)

