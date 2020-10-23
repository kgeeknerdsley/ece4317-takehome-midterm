#include <iostream>
#include <math.h>

using namespace std;

float B(float q) {

    if(q == 0 || q == 1) {
        return 0.0;
    } else {
        return -((q*log2(q)) + ((1-q)*log2(1-q)));
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

        cout << "How many categories in your attribute? : ";
        cin >> categories;
        printf("\n");

        for(int i = 0; i < categories; i++) {
            cout << "How many positive samples in category " << i << ": ";
            cin >> pk;
            //printf("\n");
            cout << "How many negative samples in category " << i << ": ";
            cin >> nk;
            printf("\n");

            remainder += ((pk+nk)/12) * B(pk/(pk+nk));
            //cout << "Remainder for cycle " << i << ": " << remainder;
        }

        gain = 1 - remainder;
        cout << "Your remainder is: " << remainder << "\n";
        cout << "Your gain is: " << gain << "\n";
    }


    

    return 0;
}