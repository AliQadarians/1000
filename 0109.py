sumGallons = sumMiles = 0
while True:
    gallon = int(input('Enter gallons used (-1 to end): '))
    if gallon == -1:
        break
    else:
        miles = int(input('Enter miles driven: '))
        rate = miles / gallon
        print('The miles / gallon for this tank was {0} .'.format(rate))
        sumGallons += gallon
        sumMiles += miles

avg = sumMiles / sumGallons
print('The overal AVG milles / gallon was {0} .'.format(avg))