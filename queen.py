class Queen:
    def __init__(self, r, c, n):
        self.rowPos = r
        self.colPos = c
        self.number = n
        self.originalRow = r
        self.originalCol = c

    def getRow(self):
        return self.rowPos

    def getCol(self):
        return self.colPos

    def getNum(self):
        return self.number

    def getOriginalRow(self):
        return self.originalRow

    def getOriginalCol(self):
        return self.originalCol

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
            if(board[self.rowPos][i] != 0):
                #print("Found a queen on the horizontal at position (" + str(self.rowPos) + "," + str(i) + ")\n")

                toAdd = tuple((self.number,board[self.rowPos][i])) #tuple is the queen hitting, and queen getting hit

                if(toAdd != (self.number, self.number)):
                    possibleHits.append(toAdd)

            #vertical motion
            if(board[i][self.colPos] != 0):
                #print("Found a queen on the vertical at position (" + str(i) + "," + str(self.colPos) + ")\n")

                toAdd = tuple((self.number,board[i][self.colPos]))

                if(toAdd != (self.number, self.number)):
                    possibleHits.append(toAdd)
        
        #yes, I know these diagonal moves are inefficient and bad

        #downward left diagonal
        diagR = self.rowPos
        diagC = self.colPos
        while(not downLeft): #downLeft goes true when we're done
            if(board[diagR][diagC] != 0):
                #print("Found a queen on the down left diagonal at position (" + str(diagR) + "," + str(diagC) + ")\n")

                toAdd = tuple((self.number,board[diagR][diagC]))

                if(toAdd != (self.number, self.number)):
                    possibleHits.append(toAdd)

            if(diagC == 0 or diagR == 7):
                downLeft = True
            else:
                diagR = diagR + 1
                diagC = diagC - 1

        #downward right diagonal
        diagR = self.rowPos
        diagC = self.colPos
        while(not downRight):
            if(board[diagR][diagC] != 0):
                #print("Found a queen on the down right diagonal at position (" + str(diagR) + "," + str(diagC) + ")\n")

                toAdd = tuple((self.number,board[diagR][diagC]))

                if(toAdd != (self.number, self.number)):
                    possibleHits.append(toAdd)

            if(diagC == 7 or diagR == 7):
                downRight = True
            else:
                diagR = diagR + 1
                diagC = diagC + 1

        #upward left diagonal
        diagR = self.rowPos
        diagC = self.colPos
        while(not upLeft):
            if(board[diagR][diagC] != 0):
                #print("Found a queen on the upper left diagonal at position (" + str(diagR) + "," + str(diagC) + ")\n")

                toAdd = tuple((self.number,board[diagR][diagC]))

                if(toAdd != (self.number, self.number)):
                    possibleHits.append(toAdd)

            if(diagC == 0 or diagR == 0):
                upLeft = True
            else:
                diagR = diagR - 1
                diagC = diagC - 1

        #upward right diagonal
        diagR = self.rowPos
        diagC = self.colPos
        while(not upRight):
            if(board[diagR][diagC] != 0):
                #print("Found a queen on the upper right diagonal at position (" + str(diagR) + "," + str(diagC) + ")\n")

                toAdd = tuple((self.number,board[diagR][diagC]))

                if(toAdd != (self.number, self.number)):
                    possibleHits.append(toAdd)

            if(diagC == 7 or diagR == 0):
                upRight = True
            else:
                diagR = diagR - 1
                diagC = diagC + 1

        return possibleHits