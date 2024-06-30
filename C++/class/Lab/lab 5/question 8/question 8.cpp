#include <iostream>
using namespace std;
double add(double num1, double num2);
double sub(double num1, double num2);
double mult(double num1, double num2);
double divide(double num1, double num2);
double modulus(int num1, int num2);
bool menu();
void main()
{
    bool ans;
    do
    {
        ans = menu();
    } while (ans);
    cout << " Thank you for using my code !" << endl;
    system("pause");
}
bool menu()
{
    int N, M;
    int choice;
    cout << "Menu\nPlease make a selection from the menu\n\t1- add two number\n\t2- subtract two number\n\t3- multiply two numbers\n\t4- divide two numbers\n\t5- modulus two numbers\n\t6- Exit\n Your Choice : ";
    cin >> choice;
    if (choice < 6 && choice > 0)
    {
        cout << "enter two numbers : ";
        cin >> N >> M;
        cout << "Result is : ";
    }
    switch (choice) // controlling expression
    {
    case 1:
        cout << add(N, M) << endl;
        return true;
    case 2:
        cout << sub(N, M) << endl;
        return true;
    case 3:
        cout << mult(N, M) << endl;
        return true;
    case 4:
        cout << divide(N, M) << endl;
        return true;
    case 5:
        cout << modulus((int)N, (int)M) << endl;
        return true;
    case 6:
        return false;
    default:
        cout << "Invalid Input" << endl;
        return true;
    }
}

double add(double num1, double num2)
{
    return num1 + num2;
}
double sub(double num1, double num2)
{
    return num1 - num2;
}
double mult(double num1, double num2)
{
    return num1 * num2;
}
double divide(double num1, double num2)
{
    return num1 / num2;
}
double modulus(int num1, int num2)
{
    return num1 % num2;
}


