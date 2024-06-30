#include <iostream>

using namespace std;

void main(){
    char userAns;
    do
    {
        double avg;
        for (int i = 0; i < 3; i++)
        {
            double temp;
            cout << "enter the #" << i+1 << " temp: ";
            cin >> temp;
            avg+=temp;
        }
        avg/=3.0;
        cout << "The average tempreture is : " << avg << endl;
        cout << "Do you want to repeat ? (y/n) :";
        cin >> userAns;
        avg = 0;
    } while (userAns == 'y');
    system("pause");
}