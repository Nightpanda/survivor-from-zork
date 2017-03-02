board = {'a': {'1': 1, '2': 1, '3': 1, '4': 1},
         'b': {'1': 1, '2': 1, '3': 1, '4': 1},
         'c': {'1': 1, '2': 1, '3': 1, '4': 1},
         'd': {'1': 1, '2': 1, '3': 1, '4': 1}}

gameOver=False

def drawBoard():
    print '  1  2  3  4'
    for row in board:
        drawnRow = row
        for square in board[row]:
            if board[row][square] == 1:
                drawnRow = drawnRow + ' X '
            else:
                drawnRow = drawnRow + ' O '
        print drawnRow

def moveWizard():
    move=raw_input("Where to move Wizard?")


def moveMage():
    move=raw_input("Where to move Mage?")

while not gameOver:
    moveWizard()
    moveMage()
    drawBoard()
