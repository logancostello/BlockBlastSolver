
# Functions to check for and clear full rows and columns
def clearRow(game, row):
    if row < len(game):
        game[row] = [0] * len(game[row])
    else:
        raise Exception("Row not valid: ", row)

def clearCol(game, col):
    if col < len(game[0]):
        for row in range(len(game)):
            game[row][col] = 0
    else:
        raise Exception("Column not valid", col)

def checkClear(game):
    rowsToClear = []
    colsToClear = []

    for row in range(len(game)):
        if sum(game[row]) == len(game[row]):
            rowsToClear.append(row)

    for col in range(len(game[0])):
        full = True
        for row in range(len(game)):
            if game[row][col] == 0:
                full = False
                break

        if full:
            colsToClear.append(col)
   
    for row in rowsToClear:
        clearRow(game, row)
    
    for col in colsToClear:
        clearCol(game, col)

# Function to create an empty game
def createGame(numRows, numCols):
    if numRows > 0 and numCols > 0:
        return [[0] * numCols for r in range(numRows)] 
    else:
        raise Exception("Dimensions must be > 0")

# Function to check if a piece can be played at a coordinate
# A piece is a list of coordinates: [row, col]
# The row and col indicate the top left coordinate if the block was a rectangle
def canPlayPiece(game, desiredRow, desiredCol, piece):
    for rowOffset, colOffset in piece:
        row = desiredRow + rowOffset
        col = desiredCol + colOffset
        if row >= len(game) or col >= len(game[0]) or game[row][col]:
            return False
    return True

# Function to play a piece
# Assumes it is safe to do so
def playPiece(game, desiredRow, desiredCol, piece):
    for rowOffset, colOffset in piece:
        row = desiredRow + rowOffset
        col = desiredCol + colOffset
        game[row][col] = 1



