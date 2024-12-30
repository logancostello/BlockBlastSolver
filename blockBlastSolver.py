
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
