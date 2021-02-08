public class Ellipsoid {
    double x;
    double y;
    double z;
    public static double volume(double _x, double _y, double _z) {
        return (4/3.0)*Math.PI*_x*_y*_z;
    }
    public static void main(String[] args) {
        Ellipsoid eggEllipsoid = new Ellipsoid();
        eggEllipsoid.x = 10;
        eggEllipsoid.y = 8;
        eggEllipsoid.z = 4;
        System.out.println("the first axis : " + eggEllipsoid.x);
        System.out.println("the second axis : " + eggEllipsoid.y);
        System.out.println("the third axis : " + eggEllipsoid.z);
        System.out.println("The Volume is " + volume(eggEllipsoid.x, eggEllipsoid.y, eggEllipsoid.z));
    }
    
}
/**

 */