#include <iostream>
using namespace std;
int powerTo(double number, int power);
void main(){
    double Num;
    int power;
    cout << "enter a number and a power : ";
    cin >> Num >> power;
    cout << Num << " to the power of " << power << " is " << powerTo(Num, power);
}
int powerTo(double number, int power){
    if (power < 0)
        return 0;
    int sum = 1;
    for (int i = 0; i < power; i++)
    {
        sum *= number;
    }
    return sum;
}