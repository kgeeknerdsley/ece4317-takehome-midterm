from queen import Queen

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
]

heuristicBoard = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
]

def printBoard():
    for row in board:
        print(row)

#master list to hold all queen objects
queens = [Queen(4,0), Queen(5,1), Queen(6,2), Queen(3,3), Queen(4,4), Queen(5,5), Queen(6,6), Queen(5,7)]

#place all queens in the appropriate spot
for i in range(len(queens)):
    board[queens[i].getRow()][queens[i].getCol()] = 1

printBoard()

test = queens[3].findHitPairs(board)
print(test)
x = test[1]
x = x[::-1]
print(x)





#find the new spot
# set the appropriate queen's location
# foreach through the list of queens, generating their list of hits
# compare each list to the master hit list, eliminating duplicates
# print final number to the spot in completedBoard
# reset queen positions, empty lists, change spot