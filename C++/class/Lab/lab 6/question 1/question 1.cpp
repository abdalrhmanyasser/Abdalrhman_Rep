#include <iostream>

using namespace std;

void sort3(double& num1, double& num2, double& num3);

void main(){
    double a, b, c;
    cout << "enter your 3 numbers to be sorted : ";
    cin >> a >> b >> c;
    sort3(a, b, c);
    cout << "\nNumbers sorted lowest to highest : \n";
    cout << "a : " << a << endl;
    cout << "b : " << b << endl;
    cout << "c : " << c << endl;
}
void sort3(double& num1, double& num2, double& num3){
    double temp;
    if (num3 < num2)
    {
        temp = num3;
        num3 = num2;
        num2 = temp;
    }
    if (num3 < num1)
    {
        temp = num3;
        num3 = num1;
        num1 = temp;
    }
    if (num2 < num1)
    {
        temp = num2;
        num2 = num1;
        num1 = temp;
    }
}