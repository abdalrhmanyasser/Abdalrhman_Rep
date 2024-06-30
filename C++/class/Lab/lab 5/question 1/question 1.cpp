#include <iostream>
using namespace std;
int signOf(int Num);
void main(){
    int Num;
    cout << "enter a number : ";
    cin >> Num;
    cout << signOf(Num);
}
int signOf(int Num){
    return (Num >= 0 ? Num == 0 ? 0 : 1 : -1);
}