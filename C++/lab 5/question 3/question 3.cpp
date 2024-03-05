#include <iostream>
using namespace std;
int max(double Num1, double Num2);
void main(){
    int num1, num2;
    cout << "enter two numbers : ";
    cin >> num1 >> num2;
    cout << "The bigger number is : " << max(num1, num2);
}
int max(double Num1, double Num2){
    return (Num1 > Num2 ? Num1 : Num2);
}