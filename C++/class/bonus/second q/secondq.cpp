#include <iostream>

using namespace std;

void main(){
    double sum = 0;
    for (double i = 0.01; i < 1; i+=0.01)
    {
        sum += i;
        cout<<i<<endl;
    }
    cout << "sum is : " << sum;
}