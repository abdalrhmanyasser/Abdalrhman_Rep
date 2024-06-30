#include <iostream>

using namespace std;

void read(double& num1);
void convert(double& num1);
void display(double num1);

void main(){
    double a;
    read(a);
    convert(a);
    display(a);
}
void read(double& num1){
    cout << "Enter the temperature : ";
    cin >> num1;
}
void convert(double& num1){
    num1 = num1 * (9.0f/5.0f) + 32;
}
void display(double num1){
    cout << "the temperature in F is " << num1;
}