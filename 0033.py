number = int(input('Enter number(XXXXX): '))
a1 = number % 10
number //= 10
a10 = number % 10
number //= 10
a100 = number % 10
number //= 10
a1000 = number % 10
a10000 = number // 10

print(a10000,'   ',a1000,'   ',a100,'   ', a10,'   ',a1)