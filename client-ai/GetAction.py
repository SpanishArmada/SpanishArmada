dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def inBoard(numRows, numCols, row, col):
    return ((0 <= row < numRows) and (0 <= col < numCols))

def getAction(numRows, numCols, gameState, checked):
    for i in range(numRows):
        for j in range(numCols):
            print(i, j)
            curGrid = gameState[i][j]
            if(curGrid == -1 or curGrid >= 9 or checked[i][j]):
                continue
            walls = 0
            revealedBombs = 0
            for k in range(len(dr)):
                if(inBoard(numRows, numCols, i + dr[k], j + dc[k])):
                    if(0 <= gameState[i + dr[k]][j + dc[k]] <= 8):
                        walls += 1
                    elif(gameState[i + dr[k]][j + dc[k]] >= 9):
                        revealedBombs += 1
                else:
                    walls += 1
            
            space = 8 - walls - revealedBombs
            curGrid -= revealedBombs
            print(i, j, walls, revealedBombs, space, curGrid)
            if(space == 0):
                continue
            if(curGrid == 0):
                # openGrid
                checked[i][j] = True
                actionList = ['open']
                for k in range(len(dr)):
                    if(inBoard(numRows, numCols, i + dr[k], j + dc[k])):
                        if(gameState[i + dr[k]][j + dc[k]] == -1):
                            actionList.append([i + dr[k], j + dc[k]])
                return actionList, checked
            elif(curGrid == space):
                # flagGrid
                checked[i][j] = True
                actionList = ['flag']
                for k in range(len(dr)):
                    if(inBoard(numRows, numCols, i + dr[k], j + dc[k])):
                        if(gameState[i + dr[k]][j + dc[k]] == -1):
                            actionList.append([i + dr[k], j + dc[k]])
                return actionList, checked
    return ['finish'], checked
