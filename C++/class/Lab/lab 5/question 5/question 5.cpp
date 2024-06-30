#include <iostream>
using namespace std;
double factorial(int Num);
void main(){
    int Num;
    cout << "enter a number : ";
    cin >> Num;
    cout.precision(0);
    cout << fixed << factorial(Num);
}
double factorial(int Num){
    double sum = 1;
    for (int i = 2; i <= Num; i++)
    {
        sum *= i;
    }
    return sum;
}