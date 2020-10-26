//For question 1c, by Kevin Worsley
//ECE 4317 Takehome Midterm, Fall 2020

#include <iostream>

using namespace std;

int main()
{
    int amt = 0;
    int result; //the X value
    int val = 0;
	char stopCond = 'a';
    bool stop = false;
    
    while(!stop) {
        cout << "How many piles? : ";
        cin >> amt;
        
        int values [amt] = {};
    
        //loop over and assign a value to each pile
        for(int i = 0; i < amt; i++) {
            cout << "Enter value for pile " << i + 1 << ": ";
            cin >> val;
            
            values[i] = val;
            
            if(i == 0) {
                result = val;
            } else {
                result = result ^ val; //xor all the piles together, for nimsum
            }
        }
    
        cout << "Nimsum (total XOR) is: " << result << "\n";
        
        //XOR each pile by the nimsum to get the recommended move
        for(int j = 0; j < amt; j++) {
            cout << "XOR for pile of " << values[j] <<" is " << (values[j] ^ result) << "\n";
        }
		
		cout << "Stop? Y or N : ";
		cin >> stopCond;
		
		if(stopCond == 'Y' || stopCond == 'y') {
			stop = true;
			cout << "\n";
		} else {
			stop = false;
		}
    }
    return 0;
}
