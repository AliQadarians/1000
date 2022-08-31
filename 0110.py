number = int(input('Enter a number: '))
print('I\tI*10\tI*100\tI*1000')
for i in range(1,number+1):
    print('{0}\t{1}\t{2}\t{3}'.format(i,i*10,i*100,i*1000))
exit(0)