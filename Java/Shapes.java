public class Shapes {
    double length;
    double width;
    double height;
    
    public Shapes(Double l, Double w, Double h) {
        this.length = l;
        this.width = w;
        this.height = h;
    }

    public static double volume(double l, double w, double h) {
        return l*w*h;
    }
    public static void main(String[] args) {
        Shapes rectangleShapes = new Shapes(7.0, 5.3, 10.0);
        System.out.println("the length is " + rectangleShapes.length);
        System.out.println("the width is " + rectangleShapes.width);
        System.out.println("the height is " + rectangleShapes.height);
        System.out.println("the volume is " + volume(rectangleShapes.length, rectangleShapes.width, rectangleShapes.height));
    }
}
