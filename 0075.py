import datetime
n = int(input('Enter n: '))
x = datetime.datetime.now()

y = x + datetime.timedelta(0,n)

print('{0} to {1}'.format(x.time(),y.time()))