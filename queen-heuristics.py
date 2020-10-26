#For question 3b and 3c, by Kevin Worsley
#Debugging and verification by Cristian Mejia
#ECE 4317 Takehome Midterm, Fall 2020

from queen import Queen
import pygame
from pygame.locals import *

foundDuplicate = False

#3a) Generate heuristic like textbook figure

#board used to move queens around
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
]

#holds the results of the heuristics for easy printing
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
verifiedHits = [] #holds all our confirmed hits

#place all queens in the appropriate spot
for i in range(len(queens)):
    board[queens[i].getRow()][queens[i].getCol()] = queens[i].getNum()

print("Starting board: \n")
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
        board[queens[column-1].getOriginalRow()][queens[column-1].getOriginalCol()] = column #get the position to save last column's piece
        queens[column-1].setPosition(queens[column-1].getOriginalRow(),
                                        queens[column-1].getOriginalCol()) #rowPos, colPos is fixed

    lastRPos = queens[column].originalRow #last known position of current column was original spot
    lastCPos = queens[column].originalCol
    
    for row in range(8):
        verifiedHits = []#reset verifiedHits for the new run
        queens[column].setPosition(row, column) #queen object now knows their new spot
        board[row][column] = column+1 #set the new piece in board
        board[lastRPos][lastCPos] = 0 #unset the last piece's position
        
        #determine the heuristic for the square at [row, column]
        heuristic = 0
        for j in range(len(queens)): #for the entire queen list, find the hits
            queenHitList = []
            queenHitList = queens[j].findHitPairs(board) #get the list of hit pairs
            heuristic = len(queenHitList) + heuristic #add up the heuristic value for every pair we find

        heuristicBoard[row][column] = heuristic #assign heuristic to its board

        lastRPos = row #save current positions for next run
        lastCPos = column

print("\n")
printBoard(heuristicBoard)

#The chessboard code was adapted from:
#https://stackoverflow.com/questions/45945254/make-a-88-chessboard-in-pygame-with-python
#All other graphics were written original

#3b: Make a prettier version of the output
pygame.init()
S_WIDTH = 700
S_LENGTH = 700

screen = pygame.display.set_mode((S_WIDTH, S_LENGTH))
pygame.display.set_caption("Chessboard")

size = 70
lb = (209, 196, 132) #light brown color
db = (122, 105, 18) #dark brown color
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

        number = text.render(str(heuristicBoard[i-1][z-1]), True, black) #draw text for the heuristic at [row,col]
        screen.blit(number,(size*z+5,size*i+5)) #render screen

        for queensToDraw in range(len(queens)):
            qRow = queens[queensToDraw].getOriginalRow()
            qCol = queens[queensToDraw].getOriginalCol()

            if(i-1 == qRow and z-1 == qCol): #if a square matches our queen location, draw the picture
                screen.blit(queenImage, (size*z+30,size*i+30))
        cnt +=1
    cnt-=1

pygame.draw.rect(screen,black,[size,size,boardLength*size,boardLength*size],1) #draw the border around chessboard

while(1):
    pygame.display.update()
