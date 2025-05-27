#include <iostream>
using namespace std;
class Shape{
public:
    double virtual calcArea(){return -1;}
};
class Circle : public Shape {
    private:
    int radius;
    public:
    Circle(int r) : radius(r){}
    double virtual calcArea(){
        double pi = 2 * asin(1.0); 
        return pi * pow(radius, 2);
    }
};
class Rectangle : public Shape {
    private:
    int Width;
    int Height;
    public:
    Rectangle(int w, int h) : Width(w), Height(h){}
    double virtual calcArea(){
        return Width * Height;
    }
};
class Triangle : public Shape{
private:
    int base;
    int height;
public:
    Triangle(int b, int h) : base(b), height(h){}
    double virtual calcArea(){
        return (0.5) * base * height;
    }
};

int main(){
    int w, h;
    cout << "Enter the width for the rectangle: ";
    cin >> w;
    cout << "Enter the height for the rectangle: ";
    cin >> h;
    if (w < 0 || h < 0){
        throw std::invalid_argument("Recieved a negative value");
    }
    Rectangle rect = Rectangle(w, h);
    cout << "The area of the rectangle with width 5, and height 10 : " << rect.calcArea() << endl;
    Circle circ = Circle(5);
    cout << "The area of the circle with radius 5 : " << circ.calcArea() << endl;
    Triangle triang = Triangle(5, 4);
    cout << "The area of the triangle with base 5 and height 4 : " << triang.calcArea() << endl;
}