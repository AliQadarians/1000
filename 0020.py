print('1/R = 1/R1 + 1/R2 + 1/R3')
r1 = float(input('Enter R1: '))
r2 = float(input('Enter R2: '))
r3 = float(input('Enter R3: '))

r = ( r1 * r2 *r3 ) / ( r2 * r3 + r1 * r3 + r1 * r2 )

print('R = ', r)
