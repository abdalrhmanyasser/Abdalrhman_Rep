public class Speed {
    double time;
    double distance;
    public Speed(double _distance, double _time){
        distance = _distance;
        time = _time;
    }
    public double carSpeed() { 
        return distance / time; 
    }
    public void set(double ds, double ts) {
        distance = ds;
        time = ts;
    }
    public String get(){
        return ("The distance is " + distance + " Km\nThe time is " + time + " Hours");
    }
    public static void main(String[] args) {
        Speed car = new Speed(90.0, 3.0);
        System.out.println(car.get());
        System.out.println("car speed : " + car.carSpeed() + " Km/H");
    }
}
