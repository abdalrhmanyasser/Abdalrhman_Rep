public class Student{
    float aiMark;
    float mathMark;
    float average;
    static float marksAverage (float x, float y){
        return (x+y)/2.0f;
    }
    public static void main(String[] args) {
        Student me = new Student();
        me.mathMark = 90;
        me.aiMark = 95;
        me.average = marksAverage(me.aiMark, me.mathMark);
        System.out.println(me.aiMark + " " + me.mathMark + " " + me.average);
    }
}