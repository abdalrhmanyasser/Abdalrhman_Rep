#include <iostream>
using namespace std;
char signOf(double Num1);
void main(){
    int Num1;
    cout << "enter a number to check its sign : ";
    cin >> Num1;
    cout << signOf(Num1);
}
char signOf(double Num1){
    return (Num1 <= 0 ? 'N' : 'P');
}