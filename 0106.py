cost = int(input('Enter cost: '))
for i in range(1,11):
    cost -= (cost * 0.2)
    print('year = {0}\tcost={1}'.format(i,cost))
