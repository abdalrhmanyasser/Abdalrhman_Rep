#include <iostream>
#include <string>
using namespace std;
const float PI = 3.14159265f;
class Shape{
    public:
    string m_name;
    int Area;
    int Circumfrunce;
    double getArea() {
        return 0;
    };
    double getCircumfrunce(){
        return 0;
    };
    public:
    Shape(string Name): m_name(Name){}
    Shape(){}
};
class Circle : Shape{
    private:
    int radius;
    public:
    Circle(string Name, int Radius){
        this->m_name = Name;
        this->radius = Radius;
    }
    double getArea(){
        return PI * pow(this->radius, 2);
    }
    double getCircumfrunce(){
        return 2 * PI * this->radius;
    }
};
class Rect : Shape{
    private:
    int m_Length;
    int m_Width;
    public:
    Rect(string Name, int Length, int Width) : m_Length(Length), m_Width(Width){
        this->m_name = Name;
    }
    double getArea(){
        return m_Width * m_Length;
    }
    double getCircumfrunce(){
        return m_Length * 2 + m_Width * 2;
    }
};
int main(){
    Circle circle = Circle("Big", 5);
    Rect rectangle = Rect("Hello", 10, 5);
    cout << "Circle : \n\tArea : " << circle.getArea();
    cout << "\n\tCircumfrunce : " << circle.getCircumfrunce() << endl;
    cout << "Rect : \n\tArea : " << rectangle.getArea();
    cout << "\n\tCircumfrunce : " << rectangle.getCircumfrunce() << endl;
    system("pause");
    return 0;
}