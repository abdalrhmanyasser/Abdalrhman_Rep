#include <iostream>
using namespace std;
char signOfMulti(double Num1, double Num2);
void main(){
    int Num1, Num2;
    cout << "enter two numbers : ";
    cin >> Num1 >> Num2;
    cout << "The sign of the multiplication of the two numbers is : " <<  signOfMulti(Num1, Num2);
}
char signOfMulti(double Num1, double Num2){
    int multi = Num1 * Num2;
    return (multi <= 0 ? 'N' : 'Y');
}