a4_number = 50
pen_number = 150
a4_price = float(input('Enter a4 price: '))
pen_price = float(input('Enter pen price: '))
inflation = float(input('Enter inflation:'))

inflation /= 100
cost = (a4_number * a4_price * inflation) + (pen_number * pen_price * inflation)

print('Extra cost is {} .'.format(cost))
