counter = 0
for i in range(3):
    for j in range(6):
        for k in range(11):
            for z in range(21):
                sum = i * 500 + j * 200 + k * 100 + z * 50
                if sum == 1000:
                    counter += 1
                    print('P({0}) = ( {1} * 500 + {2} * 200 + {3} * 100 + {4} * 50 )'.format(counter,i,j,k,z))