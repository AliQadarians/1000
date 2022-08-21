from imghdr import what


n = int(input('Enter count of student: '))
if n < 2 :
    print('Enter a number greater than 2.')
    exit(0)
max1 = max2 = -1
id1 = id2 = 0
i = 0
while i < n :
    id = int(input('Enter id: '))
    avg = float(input('Enter AVG: '))

    if avg > max1 :
        max1 = avg
        id1 = id
    
    if avg < max1 :
        if avg > max2 :
            max2 = avg
            id2 = id
        else: 
            pass
    i += 1

print('2th student:\nid = {0} , AVG = {1}'.format(id2,max2))
    

