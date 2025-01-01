
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

# Function to score the current state of the game
# Used for searching and evaluating future positions
def scoreCurrentState(game):
    # Each open space increases the score by 1
    # Each open neighbor of an open space increases the score by 1
    # This way, large open spaces are scored higher
    score = 0
    for row in range(len(game)):
        for col in range(len(game[0])):
            if game[row][col] == 0:
                score += 1
                if row - 1 > 0 and game[row - 1][col] == 0:
                    score += 1
                if row + 1 < len(game) and game[row + 1][col] == 0:
                    score += 1
                if col - 1 > 0 and game[row][col - 1] == 0:
                    score += 1
                if col + 1 < len(game[0]) and game[row][col + 1] == 0:
                    score += 1
    
    return score

# Find all places a piece can be played
def getAllPossibleMoves(game, piece):
    possibleMoves = []
    for row in range(len(game)):
        for col in range(len(game[0])):
            if canPlayPiece(game, row, col, piece):
                possibleMoves.append([row, col])
    
    return possibleMoves

# Given a game and a piece, find the best spot to play it
def findBestMove(game, piece):
    possibleMoves = getAllPossibleMoves(game, piece)
    scores = []

    for row, col in possibleMoves:
        gameCopy = game
        playPiece(gameCopy, row, col, piece)
        checkClear(gameCopy)
        score = scoreCurrentState(game)
        scores.append(score)

    if scores:
        maxScore = max(scores)
        return [possibleMoves[scores.index(maxScore)], maxScore]
    else:
        return [None, float("-inf")]

# Given a list of pieces, find the best way to play them the given order
# Return the positions and the final score
def findBestMovesInOrder(game, pieces):
    if len(pieces) == 1:
        pos, score = findBestMove(game, pieces[0])
        return [[pos], score]
    else:
        maxScore = float('-inf')
        bestMoves = None
        piece = pieces.pop(0)
        possibleMoves = getAllPossibleMoves(game, piece)
        for row, col in possibleMoves:
            gameCopy = game
            playPiece(gameCopy, row, col, piece)
            positions, score = findBestMovesInOrder(gameCopy, pieces)
            if score > maxScore:
                maxScore = score
                bestMoves = [[row, col]] + positions
        return [bestMoves, maxScore]



