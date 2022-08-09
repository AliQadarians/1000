bit = 80 * 30 
paper = int(input('Enter number paper: '))
volume = int(input('Enter volume of flash: '))

z = (volume * 1024**3) / (bit * paper)

print(z)