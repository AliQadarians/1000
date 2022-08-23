price = float(input('Enter price: '))
inc = float(input('Enter inc:'))
n = int(input('Enter n: '))

print('Year     Price')
for i in range(1,n+1):
    price += (price * inc / 100)
    print('{0}      {1}'.format(i,price))

exit(0)