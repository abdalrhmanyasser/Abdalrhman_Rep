#include <iostream>
#include <string.h>

using namespace std;
void main(){
    char userAns;
    do
    {
        int age;
        cout << "Enter your age : ";
        cin >> age;
        double money;
        cout << "Enter your amount of money : ";
        cin >> money;

        if (age > 18 && money < 500){
            cout << "You are allowed to participate" << endl;
        }else{
            cout << "you are not allowed" << endl;
        }
        cout<< "do you want to redo (y/n): ";
        cin >> userAns;
    } while (userAns == 'y');
    
}