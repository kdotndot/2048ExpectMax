import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
DONOTHING = 4
##Weights for score = W{1,2,3}, largest num, sum nums, empty spots
TABLELEN = 4 #TABLE length and TABLE height
moves = [UP, DOWN, LEFT, RIGHT, DONOTHING]
""" temp = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
            ] """
def printMatrix(table):
    for x in range(0, TABLELEN):
        print(table[x])
def mergeHelp(a, out):
    for i in [0,1,2,3]:
        c = 0
        for j in [0,1,2,3]:
            if a[i][j] != 0:
                out[i][c] = a[i][j]
                c += 1
    return out

def merge(a):
    for i in [0,1,2,3]:
        for j in [0,1,2]:
            if a[i][j] == a[i][j + 1] and a[i][j] != 0:
                a[i][j] *= 2
                a[i][j + 1] = 0   
    return a



def genScore(table):
    score = 0
    maxnum = 0
    empty = 0
    num = 0
    for x in range(0, TABLELEN):
        for y in range(0, TABLELEN):
            if table[y][x] > maxnum:
                maxnum = table[y][x]
            if table[y][x] == 0:
                empty += 1
            num += table[y][x]       
    
    score = maxnum + (2*num) + (3*empty)
    return score

def NextMove(table, step):
    maxscore = 0
    #Create boards for all possible moves
    numtables = 0
    scores = [0,0,0,0,0]
    
    #Find maxscore using weights for each probability of each move
    for x in range(0, len(moves)):
        mergedTable = merger(table, moves[x])
        table2, table4 = genRandBoards(mergedTable)
        numTables = len(table2) + len(table4)
        score = 0
        for y in range(0, len(table2)):
            score += (1/numTables) * .9 * genScore(table2[y])
        for y in range(0, len(table4)):
            score += (1/numTables) * .1 * genScore(table4[y])
        scores[x] = score
    print(scores)
    ind = 0
    for x in range(0, len(moves)):
        if scores[x] > maxscore:
            maxscore = scores[x]
            ind = x
    
    return ind
    
 
def merger(table, dir):
    z1 = np.zeros((4, 4))
    z2 = np.zeros((4, 4))
    table = np.array(table)
    if dir == UP:
        print(table)
        table = table[:,::-1].T
        table = mergeHelp(table, z1)
        table = merge(table)
        table = mergeHelp(table, z2)
        table = table.T[:,::-1]
    if dir == DOWN:
        table = table.T[:,::-1]
        table = mergeHelp(table, z1)
        table = merge(table)
        table = mergeHelp(table, z2)
        table = table[:,::-1].T
    if dir == LEFT:
        table = mergeHelp(table, z1)
        table = merge(table)
        table = mergeHelp(table, z2)
    if dir == RIGHT:
        table = table[:,::-1]
        table = table[::-1,:]
        table = mergeHelp(table, z1)
        table = merge(table)
        table = mergeHelp(table, z2)
        table = table[:,::-1]
        table = table[::-1,:]
    t = table.tolist()
    return t
        
##Generates random boards with 2's and 4's
#Input: Table, Output: List of tables with randomized 2s, List of tables with randomized 4s
def genRandBoards(table):
    board2 = []
    board4 = []
    for x in range(0, TABLELEN):
        for y in range(0, TABLELEN):
            if table[y][x] == 0:
                temp = table
                temp[y][x] = 2
                board2.append(temp)
                temp = table
                temp[y][x] = 4
                board4.append(temp)
    return board2, board4
    
    
if __name__ == "__main__":
    temp = [[0,64,0,4],
            [0,0,2,0],
            [0,64,2,0],
            [0,0,0,4]
            ]
    
    
    print(NextMove(temp, 0))
    
    
    
    
    
    
    