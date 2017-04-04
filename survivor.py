board = [[1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1]]

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

def wizardUp(x, y, side):
    return [(x + 1 * side), (y + 2)]

def wizardLeft(x, y, side):
    return [(x - 2), (y + 1 * side)]

def wizardRight(x, y, side):
    return [(x + 2), (y + 1 * side)]

def wizardDown(x, y, side):
    return [(x + 1 * side), (y - 2)]

def isMoveLegalWizard(curPos, move):
    moves = []
    location = curPos
    locationX = location[0]
    locationY = location[1]
    move = move.split(',')
    moveX = int(move[0])
    moveY = int(move[1])
    moves.append(wizardUp(locationX, locationY, 1))
    moves.append(wizardUp(locationX, locationY, -1))
    moves.append(wizardDown(locationX, locationY, 1))
    moves.append(wizardDown(locationX, locationY, -1))
    moves.append(wizardLeft(locationX, locationY, 1))
    moves.append(wizardLeft(locationX, locationY, -1))
    moves.append(wizardRight(locationX, locationY, 1))
    moves.append(wizardRight(locationX, locationY, -1))
    legalMoves = filter(lambda x: 4 > x[0] >= 0 and 4 > x[1] >= 0, moves)
    print legalMoves

def changeBoard(position, char):
    position = position.split(',')
    posX = int(position[0])
    posY = int(position[1])
    board[posX][posY] = char

def moveChar(char):
    curPos = findChar(char)
    if char=='W':
        move=raw_input("Where to move Wizard?")
        isMoveLegalWizard(curPos, move)
        board[curPos[0]][curPos[1]] = 0
    elif char=='M':
        move=raw_input("Where to move Mage?")
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
