#include <iostream>

using namespace std;

void time(int totalSeconds, int& hours, int& minutes, int& seconds);

void main(){
    int tot, h, m, s;
    cout << "Enter the total number of seconds passed : ";
    cin >> tot;
    time(tot, h, m, s);
    cout << "\nNumbers sorted lowest to highest : \n";
    cout << "hours\t : " << h << endl;
    cout << "minutes : " << m << endl;
    cout << "seconds : " << s << endl;
}
void time(int totalSeconds, int& hours, int& minutes, int& seconds){
    hours = totalSeconds/3600;
    minutes = (totalSeconds % 3600)/60;
    seconds = totalSeconds%60;
}