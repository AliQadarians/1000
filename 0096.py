scorPlayer1 = scorPlayer2 = 0
for i in range(1,2):
    player1 = int(input('Player1 please enter 1(sissors)/ 2(ston)/ 3(paper): '))
    player2 = int(input('Player2 please enter 1(sissors)/ 2(ston)/ 3(paper): '))
    if player1==1 and player2 ==2:
        scorPlayer2 += 1
    elif player1==1 and player2==3:
        scorPlayer1 += 1
    elif player1==2 and player2==1:
        scorPlayer1 += 1
    elif player1==2 and player2==3:
        scorPlayer2 += 1
    elif player1==3 and player2==1:
        scorPlayer2 += 1
    elif player1==3 and player2==2:
        scorPlayer1 += 1

print('ScorPlayer1 = {0}\tScorPlayer2 = {1}'.format(scorPlayer1,scorPlayer2))
if scorPlayer1 > scorPlayer2:
    print('Winer Player1')
else:
    print('Winer player2')

