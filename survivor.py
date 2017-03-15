board = [[1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1]]

def legalMovesWizard():
    if gameStart is True:
        return []
    else:
        return []

def drawBoard():
    for row in board:
        print row

def findChar(char):
    for index, val in enumerate(board):
        locationX = index
        try:
            locationY = val.index(char)
            return [locationX, locationY]
        except ValueError:
            pass

def changeBoard(position, char):
    position = position.split(',')
    posX = int(position[0])
    posY = int(position[1])
    board[posX][posY] = char

def moveChar(char):
    if char=='W':
        move=raw_input("Where to move Wizard?")
    elif char=='M':
        move=raw_input("Where to move Mage?")
    curPos = findChar(char)
    board[curPos[0]][curPos[1]] = 0
    madeMove = move.split(',')
    if board[int(madeMove[0])][int(madeMove[1])] == 0:
        print char + ' Lost the game!'
        #TODO: Call ending game here
    changeBoard(move, char)

gameOn=True
drawBoard()
move=raw_input("Where does the Wizard start?")
changeBoard(move, 'W')
drawBoard()
move=raw_input("Where does the Mage start?")
changeBoard(move, 'M')
drawBoard()

while gameOn:
    moveChar('W')
    drawBoard()
    moveChar('M')
    drawBoard()
