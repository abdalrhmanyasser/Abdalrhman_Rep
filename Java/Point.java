public class Point {
    double x;
    double y;
    public Point(double _x, double _y){
        this.x = _x;
        this.y = _y;
    }
    public static double slope(Point x, Point y) {
        return (y.y - x.y) / (y.x - x.x);
    }
    public String info(String index) {
        return "The " + index + " point is : (" + this.x + ", " + this.y + ")";
    }
    public static void main(String[] args) {
        Point point1 = new Point(2, 4);
        Point point2 = new Point(6, 10);
        System.out.println(point1.info("first"));
        System.out.println(point2.info("second"));
        System.out.println("The Slope is : "+slope(point1, point2));
    }
}
