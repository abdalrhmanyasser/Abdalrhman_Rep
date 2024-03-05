#include <iostream>
#include <string>

using namespace std;

int main () {
    string songs[10] = {"Lose Control"
            ,"Beautiful Things"
            ,"Cruel Summer"
            , "Snooze"
            , "I Remember Everything"
            , "Greedy"
            , "Fast Car"
            , "Agora Hills"
            , "Flowers"
            , "Stick Season"};
    for (int i = 0; i < 10; i++)
    {
        cout << i+1 << " " << songs[i] << endl;
    }
    int choice;
    cin >> choice;
    cout << "you chose \"" << songs[choice] << "\"" << endl;
    system("pause");
    return 0;
}