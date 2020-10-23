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
    
        for(int i = 0; i < amt; i++) {
            cout << "Enter value for pile " << i + 1 << ": ";
            cin >> val;
            
            values[i] = val;
            
            if(i == 0) {
                result = val;
            } else {
                result = result ^ val; //xor all the piles together
            }
        }
    
        cout << "Nimsum (total XOR) is: " << result << "\n";
        
        for(int j = 0; j < amt; j++) {
            cout << "XOR for pile of " << values[j] <<" is " << (values[j] ^ result) << "\n";
            //cout << "Should remove " << values[j] - (values[j] ^ result) << " sticks from pile";
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