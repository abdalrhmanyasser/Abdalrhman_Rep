public class BMI {
    double weight;
    double height;
    public static double myBMI(BMI bmi){
        return (bmi.weight / (bmi.height * bmi.height));
    }
    public static void printEverything(BMI bmi) {
        System.out.println("Weight : " + bmi.weight + "\nheight : " + bmi.height + "\nyour BMI : " + myBMI(bmi));
    }
    public static void main(String[] args) {
        BMI abdalrhman = new BMI();
        abdalrhman.weight = 74.3;
        abdalrhman.height = 1.7;
        printEverything(abdalrhman);
    }
}