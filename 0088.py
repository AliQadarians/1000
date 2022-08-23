x = float(input('Enter X: '))
s = 0 
t = 0
sig = 1

for i in range(1,11):
    for j in range(1,i+1):
        t = t + j * (x ** j)
    s = s * sig + (1.0 / t)
    t = 0 
    sig *= -1

print('s = ',s)

