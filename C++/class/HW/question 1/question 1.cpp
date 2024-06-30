#include <iostream>

using namespace std;

void opinion(int num1);

void main(){
    int a;
    cout << "Give me your opinion\n 1. Disagree\n 2. No opinion\n 3. Agree\nYour choice : ";
    cin >> a;
    opinion(a);
}
void opinion(int num1){
    if (num1 == 1)
        cout << "Disagree\n";
    else if (num1 == 2)
        cout << "No Opinion\n";
    else if (num1 == 3)
        cout << "Agree\n";
}