#include <iostream>

using namespace std;

void main(){
    int num;
    cout << "enter a num above 0 : ";
    cin >> num;
    if (num < 0){
        cout << "invalid number"<< endl;
        system("pause");
        return;
    }
    int sum = 0;
    for (int i = 1; i <= num; i++)
    {
        sum +=i;
    }
    cout << "your sum is : " << sum << endl;
    system("pause");
}