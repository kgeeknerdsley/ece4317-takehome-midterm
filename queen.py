#For question 3b and 3c, by Kevin Worsley
#Debugging and verification by Cristian Mejia
#ECE 4317 Takehome Midterm, Fall 2020

class Queen:
    def __init__(self, r, c, n):
        self.rowPos = r
        self.colPos = c
        self.number = n
        self.originalRow = r
        self.originalCol = c

    #getters and setters for position
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

    #searches all the possible paths of an individual queen
    #returns a list of hit pairs, making sure to eliminate duplicates
    #no need to search vertically or left diagonals!
    #left diagonal will only return duplicated hits, since we check all queens in algorithm
    #vertical will never return a hit since there's only one queen per column
    def findHitPairs(self, board):
        possibleHits = []
        downLeft = False
        upLeft = False
        upRight = False
        downRight = False

        diagR = 0
        diagC = 0

        for i in range(self.colPos, 8):
            #horizontal motion
            if(board[self.rowPos][i] != 0):
                toAdd = tuple((self.number,board[self.rowPos][i])) #tuple is the queen hitting, and queen getting hit

                if(toAdd != (self.number, self.number)): #make sure the hit is not the self queen
                    possibleHits.append(toAdd)

        #downward right diagonal
        diagR = self.rowPos
        diagC = self.colPos
        while(not downRight):
            if(board[diagR][diagC] != 0):
                toAdd = tuple((self.number,board[diagR][diagC]))

                if(toAdd != (self.number, self.number)):
                    possibleHits.append(toAdd)

            if(diagC == 7 or diagR == 7):
                downRight = True
            else:
                diagR = diagR + 1
                diagC = diagC + 1

        #upward right diagonal
        diagR = self.rowPos
        diagC = self.colPos
        while(not upRight):
            if(board[diagR][diagC] != 0):
                toAdd = tuple((self.number,board[diagR][diagC]))

                if(toAdd != (self.number, self.number)):
                    possibleHits.append(toAdd)

            if(diagC == 7 or diagR == 0):
                upRight = True
            else:
                diagR = diagR - 1
                diagC = diagC + 1

        return possibleHits
