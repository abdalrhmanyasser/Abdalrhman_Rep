#include <iostream>
using namespace std;
namespace Abouud
{
    void g(){
        cout << "hello";
    }
} // namespace Abouud
using namespace Abouud;
void main(){
    g();
}