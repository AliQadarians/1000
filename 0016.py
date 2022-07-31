n = int(input('n+nn+nnn\nEnter n between 1 to 9 : '))

nn = 10 * n + n
nnn = 100 * n + 10 * n + n 
y = n + nn + nnn

print('{0} + {1} + {2} = {3}'.format(n, nn, nnn, y))