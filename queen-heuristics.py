from queen import Queen

foundDuplicate = False

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

def printBoard(gameBoard):
    for row in gameBoard:
        print(row)

#master list to hold all queen objects
queens = [Queen(4,0,1), Queen(5,1,2), Queen(6,2,3), Queen(3,3,4), Queen(4,4,5), Queen(5,5,6), Queen(6,6,7), Queen(5,7,8)]
verifiedHits = []

#place all queens in the appropriate spot
for i in range(len(queens)):
    board[queens[i].getRow()][queens[i].getCol()] = queens[i].getNum()

printBoard(board)

#get the hit list for each queen
#compare each item of the queen hit list
#if that hit, reversed, is not in the list, add the forwards version

lastRPos = queens[0].originalRow
lastCPos = queens[0].originalCol

#to iterate over every square
for column in range(8):
    #reset last column's piece
    if(column != 0):
        board[7][column-1] = 0
        board[queens[column-1].getOriginalRow()][queens[column-1].getOriginalCol()] = column

    lastRPos = queens[column].originalRow #last known position of current column was original spot
    lastCPos = queens[column].originalCol
    
    for row in range(8):
        verifiedHits = []#reset verifiedHits for the new run
        queens[column].setPosition(row,column) #queen object now knows their new spot
        board[row][column] = column+1 #set the new piece in board
        board[lastRPos][lastCPos] = 0 #unset the last piece's position
        
        #getSquareVal()...............................................................................
        for j in range(len(queens)): #for the entire queen list, find the hits
            queenHitList = []
            queenHitList = queens[j].findHitPairs(board) #might need reinitialization

            for hit in range(len(queenHitList)): #for all the hits, test them
                foundDuplicate = False
                forwardHit = queenHitList[hit]
                reversedHit = forwardHit[::-1]

                for confirmedHit in range(len(verifiedHits)):# for every hit already found, check it against new hit
                    if(reversedHit == verifiedHits[confirmedHit]):
                        foundDuplicate = True

                if(not foundDuplicate):
                    verifiedHits.append(forwardHit)
        #..................................................................................................
        heuristicBoard[row][column] = len(verifiedHits)

        lastRPos = row
        lastCPos = column

print("\n")
printBoard(board)
print("\n")
printBoard(heuristicBoard)


#find the new spot
# set the appropriate queen's location
# foreach through the list of queens, generating their list of hits
# compare each list to the master hit list, eliminating duplicates
# print final number to the spot in completedBoard
# reset queen positions, empty lists, change spot