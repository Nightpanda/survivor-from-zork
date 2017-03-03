board = [[1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1]]

gameOver=False
gameStart=True
wizardPosition=[4,4]
magePosition=[4,4]

def legalMovesWizard():
    if gameStart is True:
        return []
    else:
        return []

def drawBoard():
    for row in board:
        print row

def moveWizard():
    move=raw_input("Where to move Wizard?")

def moveMage():
    move=raw_input("Where to move Mage?")

while not gameOver:
    moveWizard()
    moveMage()
    drawBoard()
