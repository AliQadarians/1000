n = int(input('Enter number of employ: '))
i = 0
while i < n:
    id = int(input('Enter Id: '))
    h = float(input('Enter houre: '))
    hp = float(input('Enter hourly wage: '))

    if h <= 40:
        p = h * hp
        ov = 0

    else: 
        p = 40 * hp
        ov = (h - 40) * 0.5 * hp

    salary = p + ov

    print('ID = {0} salary = {1} ov = {2}'.format(id,salary,ov))
    
