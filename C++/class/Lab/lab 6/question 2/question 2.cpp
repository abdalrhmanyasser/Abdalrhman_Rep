#include <iostream>

using namespace std;
void change(int money, int& hundereds, int& fifties, int& twenties, int& tens, int& fives, int& ones);

void main(){
    int a, b, c, d, e, f;
    int money;
    cout << "Enter the Amount of money you have : ";
    cin >> money;
    change(money, a, b, c, d, e, f);
    cout << "Original Number is " << money << endl;
    cout << "Hundereds: " << a << endl;
    cout << "Fifties\t : " << b << endl;
    cout << "Twenties : " << c << endl;
    cout << "tens\t : " << d << endl;
    cout << "Fives\t : " << e << endl;
    cout << "ones\t : " << f << endl;
}
void change(int money, int& hundereds, int& fifties, int& twenties, int& tens, int& fives, int& ones){
    hundereds = money / 100;
    fifties = (money % 100) / 50;
    twenties = (money % 50) / 20;
    tens = (money % 20) / 10;
    fives = (money % 10) / 5;
    ones = (money % 5);
}