while True:
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
    sig = 1
    sum = 0

    if x == 0 & y == 0:
        break
    
    print('{0} * {1} ='.format(x,y),end=' ')

    if y < 0:
        y *= -1
        sig *= -1

    for i in range(1,y+1):
        sum += x
    
    sum *= sig

    print('{0}\n'.format(sum))