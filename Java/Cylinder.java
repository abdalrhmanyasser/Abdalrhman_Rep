public class Cylinder{
    int radius;
    int height;
    
    public Cylinder(int r, int h) {
        radius = r;
        height = h;
    }

    public double volume() {
        return Math.PI * Math.pow(radius, 2) * height;
    }

    public static void main(String[] args) {
        Cylinder sodaCan = new Cylinder(3, 5);
        System.out.println(sodaCan.volume());
        System.out.println((Math.pow(125, 1.0/3.0)));
        System.out.println(Math.cbrt(125));
    }
}