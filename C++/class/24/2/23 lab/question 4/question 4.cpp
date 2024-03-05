#include <iostream>

using namespace std;

void main(){
    int num;
    int max = -2147483647 - 1;
    while (1)
    {
        cout << "Enter a number :";
        cin >> num;
        if (num == 0){
            break;
        }
        max = (num > max) ? num : max;
    }
    cout << "the max number is : " << max << endl;
    system("pause");
}