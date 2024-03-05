#include <iostream>
#include <string.h>

using namespace std;
int main()
{
    char userAns;
    do
    {
        cout << "Enter your Mark : ";
        int Mark;
        cin >> Mark;
        switch (Mark)
        {
        case 100:
            cout << "You have a perfect score.\n";
            cout << "Your Grade is : A\n";
            break;
        case 80:
            cout << "Your Grade is : B\n";
            break;
        case 70:
            cout << "Your Grade is : C\n";
            break;
        case 60:
            cout << "Your Grade is : D\n";
            break;
        case 50:
            cout << "Your Grade is : F\n";
        }
        cout << "Do you want to repeat.\n";
        cin >> userAns;
    }while (userAns == 'y');
    return 0;
}