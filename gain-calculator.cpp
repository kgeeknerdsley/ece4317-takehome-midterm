//For question 4, by Kevin Worsley
//ECE 4317 Takehome Midterm, Fall 2020

#include <iostream>
#include <math.h>

using namespace std;

float B(float q) {

    if(q == 0 || q == 1) {
        return 0.0; //if B is given 0 or 1, it tries to calculate log2(0) which is undefined. just set to 0 instead
    } else {
        return -((q*log2(q)) + ((1-q)*log2(1-q))); //B formula from textbook
    }
}

int main() {
    int t = 12;
    int p = 6;
    int n = 6;

    int categories = 0;
    float pk = 0;
    float nk = 0;

    float remainder = 0.0;
    float remainderCoeff = 0.0;

    float gain = 0.0;

    while(1) {
        remainder = 0.0;
        gain = 0.0;

        //check categories amount
        cout << "How many categories in your attribute? : ";
        cin >> categories;
        printf("\n");

        //for each category, get the amount of negative and positive samples. generates pk and nk
        for(int i = 0; i < categories; i++) {
            cout << "How many positive samples in category " << i << ": ";
            cin >> pk;
            cout << "How many negative samples in category " << i << ": ";
            cin >> nk;
            printf("\n");

            remainder += ((pk+nk)/12) * B(pk/(pk+nk)); //generate remainder based on formula
        }

        gain = 1 - remainder;
        cout << "Your remainder is: " << remainder << "\n";
        cout << "Your gain is: " << gain << "\n";
    }


    

    return 0;
}
