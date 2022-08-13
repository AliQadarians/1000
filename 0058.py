from base64 import b16decode


s1 = 13 * 16
s2 = 2 * 3 

b = s1 // s2
a = s1 % s2

print('b = {0}'.format(b))
print('a = {0}'.format(a))