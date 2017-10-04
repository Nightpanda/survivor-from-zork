import sys

board = [[1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1]]

def drawBoard():
    for row in board:
        print row

def moveToCoordinates(move):
    move = move.split(',')
    moveX = int(move[0])
    moveY = int(move[1])
    return [moveX,moveY]

def findChar(char):
    for index, val in enumerate(board):
        locationX = index
        try:
            locationY = val.index(char)
            return [locationX, locationY]
        except ValueError:
            pass

def isCoordinateOutsideGrid(move):
    return len([coordinate for coordinate in move if not (coordinate < 0 or coordinate > 3) ]) < 2

def wizardUp(x, y, side):
    endLocation = [(x + 1 * side), (y + 2)]
    if not isCoordinateOutsideGrid(endLocation):
        return endLocation

def wizardLeft(x, y, side):
    endLocation = [(x - 2), (y + 1 * side)]
    if not isCoordinateOutsideGrid(endLocation):
        return endLocation

def wizardRight(x, y, side):
    endLocation = [(x + 2), (y + 1 * side)]
    if not isCoordinateOutsideGrid(endLocation):
        return endLocation

def wizardDown(x, y, side):
    endLocation = [(x + 1 * side), (y - 2)]
    if not isCoordinateOutsideGrid(endLocation):
        return endLocation

def wizardLegalMovesFor(currentPosition):
    moves = []
    locationX = currentPosition[0]
    locationY = currentPosition[1]
    moves.append(wizardUp(locationX, locationY, 1))
    moves.append(wizardUp(locationX, locationY, -1))
    moves.append(wizardDown(locationX, locationY, 1))
    moves.append(wizardDown(locationX, locationY, -1))
    moves.append(wizardLeft(locationX, locationY, 1))
    moves.append(wizardLeft(locationX, locationY, -1))
    moves.append(wizardRight(locationX, locationY, 1))
    moves.append(wizardRight(locationX, locationY, -1))
    return filter(None, moves)

def isMoveLegalWizard(curPos, move):
    legalMoves = wizardLegalMovesFor(curPos)
    return moveToCoordinates(move) in legalMoves

def isMoveLegalMage(move, board):
    coordinates = moveToCoordinates(move)
    charAtLocation = board[coordinates[0]][coordinates[1]]
    if charAtLocation == 0 or charAtLocation == 'W':
        return False
    else:
        return True

def changeBoard(position, char):
    position = position.split(',')
    posX = int(position[0])
    posY = int(position[1])
    board[posX][posY] = char
    return board

def endGame(char):
    print char + ' Lost the game!'
    sys.exit()

def moveChar(char):
    curPos = findChar(char)
    if char=='W':
        move=raw_input("Where to move Wizard?")
        if isMoveLegalWizard(curPos, move):
            board[curPos[0]][curPos[1]] = 0
        else:
            endGame(char)
    elif char=='M':
        move=raw_input("Where to move Mage?")
        if isMoveLegalMage(move, board):
            board[curPos[0]][curPos[1]] = 0
        else:
            endGame(char)
    madeMove = move.split(',')
    if board[int(madeMove[0])][int(madeMove[1])] == 0:
        endGame(char)
    else:
        changeBoard(move, char)

def main():
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


if __name__ == "__main__":
   main()
