while True:
    m = int(input('M: '))
    tedad = int(input('tadad: '))
    s = float(input('S: '))

    k = m * (tedad+1) * s / 2400
    v = m + k
    p = v / tedad

    print('mablagh vam = ',v)
    print('mablagh ghest = ',p)

    ansi = input('Do you like to continue(y/n):')
    if ansi == 'y' or ansi == 'Y':
        continue
    else:
        break

exit(0)