class Queen:
    def __init__(self, r, c):
        self.rowPos = r
        self.colPos = c

    def getRow(self):
        return self.rowPos

    def getCol(self):
        return self.colPos

    def setPosition(self, r, c):
        self.rowPos = r
        self.colPos = c

    def findHitPairs(self, board):
        possibleHits = []
        downLeft = False
        upLeft = False
        upRight = False
        downRight = False

        diagR = 0
        diagC = 0

        for i in range(8):
            #horizontal motion
            if(board[self.rowPos][i] == 1):
                print("Found a queen on the horizontal at position (" + str(self.rowPos) + "," + str(i) + ")\n")

                toAdd = tuple((self.rowPos,i))

                if(toAdd != (self.rowPos, self.colPos)):
                    possibleHits.append(toAdd)

            #vertical motion
            if(board[i][self.colPos] == 1):
                print("Found a queen on the vertical at position (" + str(i) + "," + str(self.colPos) + ")\n")

                toAdd = tuple((i,self.colPos))

                if(toAdd != (self.rowPos, self.colPos)):
                    possibleHits.append(toAdd)
        
        #downward left diagonal
        diagR = self.rowPos
        diagC = self.colPos
        while(not downLeft): #downLeft goes true when we're done
            if(board[diagR][diagC] == 1):
                print("Found a queen on the down left diagonal at position (" + str(diagR) + "," + str(diagC) + ")\n")

                toAdd = tuple((self.rowPos,i))

                if(toAdd != (self.rowPos, self.colPos)):
                    possibleHits.append(toAdd)

            if(diagC == 0):
                downLeft = True
            else:
                diagR = diagR + 1
                diagC = diagC - 1
                
            

            



        return possibleHits
