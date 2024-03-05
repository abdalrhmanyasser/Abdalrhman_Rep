#include <iostream>
using namespace std;
int signOf(double Num1);
double absolute(double num1);
void main(){
    int Num1;
    cout << "enter a number to find its absolute : ";
    cin >> Num1;
    
    cout << "absolute is : " << absolute(Num1);
}
double absolute(double num1){
    return num1 / signOf(num1); 
}
int signOf(double Num1){
    return (Num1 <= 0 ? -1 : 1);
}