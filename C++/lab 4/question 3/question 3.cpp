#include <iostream>

using namespace std;
void main(){
    for (int i = 0; i < 15; i++)
    {
        char letter;
        cout << i+1 << ". Enter a letter other than A : ";
        cin >> letter;
        if (letter == 'A' || letter == 'a'){
            cout << "Hey! you weren't supposed to enter A!" << endl;
            return;
        }
    }
    cout << "Wow, you're more patient then I am, you win." << endl;
    system("pause");
}