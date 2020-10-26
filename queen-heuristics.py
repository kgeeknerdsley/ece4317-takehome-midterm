from queen import Queen
import pygame
from pygame.locals import *

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

#https://stackoverflow.com/questions/45945254/make-a-88-chessboard-in-pygame-with-python

#3b: Make a prettier version of the output
pygame.init()
S_WIDTH = 700
S_LENGTH = 700

screen = pygame.display.set_mode((S_WIDTH, S_LENGTH))
pygame.display.set_caption("Chessboard")

size = 70
lb = (209, 196, 132)
db = (122, 105, 18)
black = (0,0,0)
white= (255,255,255)

#board length, must be even
boardLength = 8
screen.fill((255,255,255))

text = pygame.font.Font(None, 36)
queenImage = pygame.image.load('queen.png')

cnt = 0
for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        #check if current loop value is even
        if cnt % 2 == 0:
            pygame.draw.rect(screen, lb,[size*z,size*i,size,size])
        else:
            pygame.draw.rect(screen, db, [size*z,size*i,size,size])

        number = text.render(str(heuristicBoard[i-1][z-1]), True, black)
        screen.blit(number,(size*z+5,size*i+5))

        for queensToDraw in range(len(queens)):
            qRow = queens[queensToDraw].getOriginalRow()
            qCol = queens[queensToDraw].getOriginalCol()

            if(i-1 == qRow and z-1 == qCol):
                screen.blit(queenImage, (size*z+30,size*i+30))
        cnt +=1
    #since theres an even number of squares go back one value
    #screen.blit(number,(size*i,size*z))
    cnt-=1
#Add a nice boarder
pygame.draw.rect(screen,black,[size,size,boardLength*size,boardLength*size],1)

while(1):
    pygame.display.update()