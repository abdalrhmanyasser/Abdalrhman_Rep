#include <iostream>
#include <string>

using namespace std;

void main(){
    string userName;
    int num;
    cout << "What is your name:";
    cin >> userName;
    cout << "How many times you wish to print a greeting to you: ";
    cin >> num;
    for (int i = 0; i < num; i++)
    {
        cout << "Hello " << userName << endl;
    }
    system("pause");
}