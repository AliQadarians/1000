while True:
    ch = input('Enter a char: ')
    if ch[0]=='w' or ch[0]=='W':
        print('You love white color.')
    elif ch[0]=='r' or ch[0]=='R':
        print('You love Red color.')
    elif ch[0]=='y' or ch[0]=='Y':
        print('You love yellow color.')
    elif ch[0]=='b' or ch[0]=='B':
        print('You love blue color.')
    elif ch[0]=='e' or ch[0]=='E':
        print('Exit')
        break
    else:
        print('No color choosen')
exit(0)