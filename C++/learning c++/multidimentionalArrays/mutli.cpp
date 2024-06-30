#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
void main(){
    int size = 32;
    int** a3d = new int*[size];
    for (int i = 0; i < size; i++){
        a3d[i] = new int[size];
    }
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            a3d[i][j] = (i+1)*(1+j);
        }
    }
    
    for (int i = 0; i < size; i++){
        cout << "\n";
        for (int j = 0; j < size; j++){
            cout << setw(to_string(size*size).length()+1) << a3d[i][j];
        }
    }
}