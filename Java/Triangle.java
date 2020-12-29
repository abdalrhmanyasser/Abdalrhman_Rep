public class Triangle {
    float base;
    float height;
    public static float area(Triangle tri){
        return ((1/2.0f) * tri.base * tri.height);
    }
    public static void printEverything(Triangle tri) {
        System.out.println("Base : " + tri.base + "\nheight : " + tri.height + "\narea : " + area(tri));
    }
    public static void main(String[] args) {
        Triangle tri = new Triangle();
        tri.base = 14.3f;
        tri.height = 16.2f;
        printEverything(tri);
    }
}