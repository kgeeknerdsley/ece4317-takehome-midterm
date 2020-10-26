#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

//Lets the user pick the values of each pile manually
//INPUT: Takes in pile array and length
//OUTPUT: None
void manualPilePopulate(int pileArr[], int pileAmt) {
    int pileValue = 0;

    for(int i = 0; i < pileAmt; i++) {
        cout << "Enter value for pile " << i+1 << ": ";
        cin >> pileValue;

        pileArr[i] = pileValue;
    }
}

//Randomly selects the value of each pile
//INPUT: Takes in pile array and length
//OUTPUT: None
void randomPilePopulate(int pileArr[], int pileAmt) {
    for(int i = 0; i < pileAmt; i++) {
        pileArr[i] = rand() % 10 + 1;
    }
}

//Prints the current state of all the piles
//INPUT: Takes in pile array and length
//OUTPUT: None
void printPileState(int pileArr[], int pileAmt) {
    printf("\n");

    for(int i = 0; i < pileAmt; i++) {
        if(pileArr[i] == 0){
            cout << "Pile " << i+1 << " is depleted.\n";
        } else {
            cout << "Pile " << i+1 << " has " << pileArr[i] << " sticks remaining.\n";
        }
    }
}

//Checks to see if the game is finished
//INPUT: Takes in pile array and length
//OUTPUT: Boolean, true = game finished, false = game not finished
bool gameOver(int pileArr[], int pileAmt) {
    bool done = true;

    for(int i = 0; i < pileAmt; i++) {
        if(pileArr[i] != 0) {
            done = false;
        }
    }

    return done;
}

int main() {
    srand(time(NULL));
    
    int popDecision = 0;
    int firstDecision = 0;
    int pileAmt = 0;
    
    bool playerTurn = false;
    int pilesXOR = 0;
    int bestPile = 0;
    int bestMove = 0;
    int singlePileXOR = 0;
    bool foundGoodMove = false;
    int randomPile = 0;

    bool validPile = false;
    int pileChosen = 0;
    bool validPull = false;
    int pullChosen = 0;
    bool gameContinue = true;
    bool safePile = false;

    //Choose settings
    cout << "Welcome to the game! Would you like:\n";
    cout << "   1) Manually populate the piles\n";
    cout << "   2) Randomly populate the piles\n";

    cin >> popDecision;

    cout << "\nWould you like to go first?\n";
    cout << "   1) Yes\n";
    cout << "   2) No\n";

    cin >> firstDecision;

    cout << "\nHow many piles?\n";
    cout << "Enter amount: ";

    cin >> pileAmt;

    //new array with size of pile amount
    int piles [pileAmt] = {};

    if(firstDecision == 1) {
        playerTurn = true;
    }

    //select whether random or manual pile value creation
    if(popDecision == 1) {
        manualPilePopulate(piles, pileAmt);
    } else {
        randomPilePopulate(piles, pileAmt);
    }

    printPileState(piles,pileAmt);

    //game loop
    while(gameContinue) {
        if(playerTurn) { //if it's the player's turn...
            validPile = false;
            validPull = false;

            cout << "\nYour turn!\n";

            //get pile to choose from, but make sure number is okay
            while(!validPile) {
                cout << "\nPlease select the number of a pile to take from: ";
                cin >> pileChosen;

                if(pileChosen > pileAmt || pileChosen < 0 || piles[pileChosen-1] == 0) { //cannot choose invalid piles bigger or smaller than list, or if 0
                    cout << "\nThat pile number is not valid, or depleted. Choose a non-depleted pile from the list.\n";
                } else {
                    validPile = true;
                }
            }

            while(!validPull) { //must have a valid number of sticks (not bigger than pile, and greater than 0)
                cout << "Please select the number of sticks to remove from pile " << pileChosen << ": ";
                cin >> pullChosen;

                if(pullChosen > piles[pileChosen-1] || pullChosen <= 0) {
                    cout << "\nThat remove amount is not valid. Choose a value from 1 - pile size.\n";
                } else {
                    validPull = true;
                }
            }

            piles[pileChosen-1] = piles[pileChosen-1] - pullChosen; //remove our requested amount

            cout << "\nYou remove " << pullChosen << " sticks from pile " << pileChosen << ".\n";

            playerTurn = !playerTurn; //change the turn
            printPileState(piles,pileAmt);
        } else {
            //computer turn
            foundGoodMove = false;

            cout << "\nComputer's turn!\n";

            //get the global pile XOR (Nimsum)
            for(int i = 0; i < pileAmt; i++) {
                if(i == 0) {
                    pilesXOR = piles[i];
                } else {
                    pilesXOR = pilesXOR ^ piles[i];
                }
            }

            //Test the nimsum against every pile. If the move can be made, do it
            for(int x = 0; x < pileAmt; x++) {
                singlePileXOR = piles[x] ^ pilesXOR;

                if(singlePileXOR < piles[x]) { //if the XOR is smaller than current pile, that's our move
                    bestPile = x;
                    bestMove = piles[x] - singlePileXOR;
                    foundGoodMove = true;
                }
            }

            //if we couldn't make an advantageous move, make a random one
            if(foundGoodMove) {
                piles[bestPile] = piles[bestPile] - bestMove;
            } else {
                safePile = false;

                while(!safePile) {
                    randomPile = rand() % pileAmt;
                    if(piles[randomPile] != 0) {
                        safePile = true;
                    }
                }
                
                bestMove = (rand() % piles[randomPile] + 1);
                bestPile = randomPile;
                piles[randomPile] = piles[randomPile] - bestMove;
            }

            cout << "\nComputer removes " << bestMove << " sticks from pile " << bestPile + 1 << ".\n";
            

            playerTurn = !playerTurn; //change turn
            printPileState(piles,pileAmt);
        }

        if(gameOver(piles,pileAmt)) { //test if the game is over
            gameContinue = false;
        }
    }

    cout << "\nGame over!\n";
    if(playerTurn == false) {
        cout << "Player is the winner!\n";
    } else {
        cout << "Computer is the winner!\n";
    }

    return 0;
}