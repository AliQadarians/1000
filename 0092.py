n = int(input('Enter count: '))
for i in range(1,n+1):
    number = int(input('Enter {0}th number: '.format(i)))
    sum = 0
    temp = number
    while temp > 0:
        sum += temp % 10
        temp //= 10
    if sum % 9 == 0:
        print(number)
exit(0)