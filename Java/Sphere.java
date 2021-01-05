import java.lang.Math.*;
/**
 * Sphere
 */
public class Sphere {
    double radius;
    public Sphere(double _radius){
        radius = _radius;
    }
    static double area(double _radius) {
        return 4*Math.PI * Math.pow(_radius, 2);
    }
    static double volume(double _radius) {
        return 4/3.0*Math.PI * Math.pow(_radius, 3);
    }
    public static void main(String[] args) {
        Sphere ball = new Sphere(10);
        System.out.println("the radius is " + ball.radius);
        System.out.println("the volume is " + volume(ball.radius));
        System.out.println("the area is " + area(ball.radius));
    }
    
}