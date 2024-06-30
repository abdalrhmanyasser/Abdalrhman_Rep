#include <iostream>
#include <string.h>

using namespace std;
int main()
{
    char userAns;
    do
    {
        int choice;
        cout << "Menu\n 1. cm to inch.\n 2. inch to cm.\nYour choice : ";
        cin >> choice;
        double distance;
        switch (choice)
        {
        case 1:
            cout << "Enter the amount of cm : ";
            cin >> distance;
            cout << "your distance in inchs is : " << distance / 2.54 << " inchs" << endl;
            break;
        case 2:
            cout << "Enter the amount of inchs : ";
            cin >> distance;
            cout << "your distance in cm is : " << distance * 2.54 << " cm" << endl;
            break;
        default:
            cout << "error. Invalid input";
            break;
        }
        cout << "do you want to repeat: ";
        cin >> userAns;
    } while (userAns == 'y');
    
    return 0;
}
