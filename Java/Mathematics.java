public class Mathematics {
    double x;
    double y;
    public Mathematics(double _x, double _y){
        x = _x;
        y = _y;
    }
    public static void main(String[] args) {
        Mathematics math = new Mathematics(4, 9);
        System.out.println(Math.pow(math.x, 2));
        System.out.println(Math.sqrt(math.y));
        System.out.println(math.y * Math.PI);
    }
}