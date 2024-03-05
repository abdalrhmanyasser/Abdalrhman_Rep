#include <iostream>
#include <string.h>

using namespace std;
void main(){
    string Name;
    int numberOfTimes;
    cout << "Enter your name: ";
    cin >> Name;
    cout << "Enter How many times you want the name to printed: ";
    cin >> numberOfTimes;
    int c = 0;
    while (c < numberOfTimes){
        cout << Name << endl;
        c+=1;
    }


    system("pause");
}
