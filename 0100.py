n = int(input('Enter a positive number: '))
fact = 1
sum = 0
i = 1
for i in (1,n+1):
    fact *= i
    sum += (1/fact)

'''while i <=n:
    sum = (1/fact)
    i += 1
    fact *= i
'''
print(sum)