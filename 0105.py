while True:
    ch = input('Enter a char: ')
    if  ch[0]=='b' or ch[0]=='B':
        print('You selected Lady!')
    elif ch[0]=='d' or ch[0]=='D':
        print('You selected miss!')
    elif ch[0]=='p' or ch[0]=='P':
        print('You selected professer!')
    elif ch[0]=='a' or ch[0]=='A':
        print('You selected Mr!')
    elif ch[0]=='j' or ch[0]=='J':
        print('You selected excellency!')
    elif ch[0]=='m' or ch[0]=='M':
        print('You selected Wife!')
    else:
        break