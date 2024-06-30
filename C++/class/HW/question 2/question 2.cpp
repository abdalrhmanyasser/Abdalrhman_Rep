#include <iostream>

using namespace std;

void quadratic(int a, int b, int c);

void main(){
    int a, b, c;
    cout << "Enter three a b c to solve the quadratic equation of the form ax^2 + bx + c : ";
    cin >> a >> b >> c;
    quadratic(a, b, c);
}
void quadratic(int a, int b, int c){
    if (a == 0){
        cout << "no solution" << endl;
    } else if (b*b - 4*a*c < 0){
        cout << "no real solution" << endl;
    }else {
        double q = sqrt(b*b - 4*a*c);
        double x1 = (-b + q)/(2*a);
        double x2 = (-b - q)/(2*a);
        cout << "the max value of the quadratic is " << max(x1, x2)<< endl;
    }
}