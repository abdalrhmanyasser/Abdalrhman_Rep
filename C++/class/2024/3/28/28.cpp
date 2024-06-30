#include <iostream>
using namespace std;

void welcome(){
    cout << "Welcome to my code"<< endl;
}
string username(){
    string name;
    cout << "enter the name ";
    cin >> name;
    return name;
}
int Userage(){
    int age;
    cout << "enter your age ";
    cin >> age;
    return age;
}

void GetDataPizza( double& Diameter, double& price){
    cout << "Enter the diameter of the pizza and its price : ";
    cin >> Diameter >> price;
}
double UnitPricePizza(double Diameter, double price){
    double radius = Diameter / 2.0;
    double area = 3.14 * radius * radius;
    return (price / area);
}
void compare(double unitPriceB, double unitPriceS){
    if (unitPriceB < unitPriceS){
        cout << "The small pizza is the better buy" << endl;
    }else{
        
        cout << "The bigger pizza is the better buy" << endl;
    }
}
void main(){
    welcome();
    string name;
    int age;
    name = username();
    age = Userage();
    cout << "Welcome " << name << " You are " << age << " years old" << endl;
    double diamBig,  priceBig;
    cout << "Big Pizza" << endl << "\t";
    GetDataPizza(diamBig, priceBig);
    double diamSmall, priceSmall;
    cout << "Small Pizza" << endl << "\t";
    GetDataPizza(diamBig, priceBig);

    double UnitPriceB = UnitPricePizza(diamBig, priceBig);
    double UnitPriceS = UnitPricePizza(diamSmall, priceSmall);
    compare(UnitPriceB, UnitPriceS);
}