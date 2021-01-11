public class calculator {
    String CalculatorModel;
    double firstNum;
    double secondNum;
    public calculator(double _firstNum, double _secondNum, String cal_model){
        firstNum = _firstNum;
        secondNum = _secondNum;
        CalculatorModel = cal_model;
    }
    public double addNum() { return firstNum + secondNum; }
    public double subNum() { return firstNum - secondNum; }
    public double multNum() { return firstNum * secondNum; }
    public double divNum() { return firstNum / secondNum; }
    public void set(double fn, double sn, String cal_model) {
        firstNum = fn;
        secondNum = sn;
        CalculatorModel = cal_model;
    }
    public String get(){
        return "The first number is " + firstNum + "\nThe second number is " + secondNum + "\nThe Calculator Model is " + CalculatorModel;
    }
    public static void main(String[] args) {
        calculator myCalculator = new calculator(5.0, 2.0, "CASIO 9999");
        System.out.println(myCalculator.get());
        System.out.println("addtion : " + myCalculator.addNum());
        System.out.println("subtraction : " + myCalculator.subNum());
        System.out.println("multiplication : " + myCalculator.multNum());
        System.out.println("division : " + myCalculator.divNum());
    }
}
