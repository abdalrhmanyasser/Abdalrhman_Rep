#include <iostream>
#include <string.h>
using namespace std;
void main(){
    int weight;
    cout << "Enter the player's weight : ";
    cin >> weight;
    cout << "Weight Class\t\t||\tBoxer's Name" << endl;
    switch (weight)
    {
    case 47:
        cout << "Minimum Weight\t\t||\tThammanoon Niyomtrong" << endl;
        break;

    case 49:
        cout << "Light Flyweight\t\t||\tRyoichi Taguchi" << endl;
        break;

    case 50:
        cout << "Flyweight\t\t||\tDaigo Higa" << endl;
        break;

    case 52:
        cout << "Super Fly\t\t||\tweight Khalid Yafai"<< endl;
        break;

    case 53:
        cout << "Bantamweight\t\t||\tRyan Burnett"<< endl;
        break;

    case 55:
        cout << "Super Bantamweight\t||\tDaniel Roman"<< endl;
        break;

    case 57: 
        cout << "Featherweight\t\t||\tLéo Santa Cruz" << endl;
        break;

    case 59: 
        cout << "Super featherweight\t||\tAlberto Machado"<< endl;
        break;

    case 61: 
        cout << "Lightweight\t\t||\tJorge Linares"<< endl;
        break;

    case 63: 
        cout<< "Super lightweight\t||\tVACANT"<< endl;
        break;

    case 66:
        cout << "Welterweight\t\t||\tKeith Thurman"<< endl;
        break;

    case 69: 
        cout << "Super welterweight\t||\tErislandy Lara"<< endl;
        break;

    case 72: 
        cout<< "Middleweight\t\t||\tGennady Golovkin"<< endl;
        break;

    case 76:
        cout << "Super middleweight\t||\tGeorge Groves"<< endl;
        break;

    case 79:
        cout << "Light heavyweight\t||\tDmitry Bivol"<< endl;
        break;

    case 90:
        cout << "Cruiserweight\t\t||\tMurat Gassiev"<< endl;
        break;
    default:
        cout << "The weight class doesnt exist." << endl;
        break;
    }
    
    system("pause");
    return;
}