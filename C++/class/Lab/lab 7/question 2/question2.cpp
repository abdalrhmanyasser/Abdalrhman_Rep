#include <iostream>

using namespace std;
void fillTemps(double Temps[], int numOfTemps);
double convertToC(double TempK);
int index(double Temps[], int numOfTemps, double value);
void printTemps(double Temps[], int numOfTemps);
void main(){
    const int numOfTemps = 10;
    double temps[numOfTemps];
    fillTemps(temps, numOfTemps);
    for (double &i : temps)
    {
        cout << i << " C to K is : " << convertToC(i) << " K\n";
    }
    cout << "Enter a value to check : ";
    double target;
    cin >> target;
    cout << "The index of " << target << " is (if the target isnt in the array the result would be -1) : " << index(temps, numOfTemps, target) << "\n";
    printTemps(temps, numOfTemps);
}
void fillTemps(double Temps[], int numOfTemps)
{
    cout << "Enter Temps for " << numOfTemps << " temperatures :\n";
    for (int i = 0; i < numOfTemps; ++i)
    {
        cout << "Enter Temperature in K for " << i + 1 << ": ";
        cin >> Temps[i];
    }
}
double convertToC(double TempK){
    return TempK - 273.15;
}
int index(double Temps[], int numOfTemps, double value){
    for (int i = 0; i < numOfTemps; i++){
        if (Temps[i] == value)
            return i;
    }
    return -1;
}

void printTemps(double Temps[], int numOfTemps){
    cout<< "Index\t";
    for (int i = 0; i < numOfTemps; i++){
        cout << i << "\t";
    }
    cout << "\nTemps\t";
    for (int i = 0; i < numOfTemps; i++){
        cout << Temps[i] << "\t";
    }
}