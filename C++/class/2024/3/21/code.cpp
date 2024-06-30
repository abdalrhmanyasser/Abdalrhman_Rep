#include <iostream>
using namespace std;
void swap(int i, int j){
    cout << "\tInside the swap function" << endl;
    cout << "\tBefore swapping n1 is " << i << " n2 is " << endl;
    int temp = i;
    i = j;
    j = temp;

    cout << "\tAfter swapping n1 is " << i << " n2 is " << j << endl;
}
void main(){
    int num1 = 1;
    int num2 = 3;
    cout << "Before invoking the swap function num1 is " << num1 << " and num2 is " << num2 << endl;
    swap(num1, num2);
    cout << "After invoking the swap function num1 is " << num1 << " and num2 is " << num2 << endl;
}