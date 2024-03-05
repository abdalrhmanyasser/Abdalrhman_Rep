#include <iostream>

using namespace std;

void main(){
    while (true)
    {
        char userInput;
        cin >> userInput;
        if (userInput != '#'){
            cout<<userInput << endl;
        }else{
            break;
        }
    }
    
}