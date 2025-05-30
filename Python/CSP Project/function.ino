#include <Encoder.h>
#include <Servo.h>

#define BASESERVOPIN A0
#define ARM1SERVOPIN A1
#define ARM2SERVOPIN A2

#define BASEBUTTONPIN 10
#define ARM1BUTTONPIN 11
#define ARM2BUTTONPIN 12

Encoder myEnc(A6, A7);
Servo arm1servo;
Servo arm2servo;
Servo baseservo;

double x=75;
double y=0;
double z=75;
long oldPosition=0;

int angleToMicroseconds(double angle) {
  double val = 460.0 + (((2400.0 - 460.0) / 180.0) * angle);
  return (int)val;
}
void moveToAngle(double b, double a1, double a2) {
  arm1servo.writeMicroseconds(angleToMicroseconds(188 - a1));
  arm2servo.writeMicroseconds(angleToMicroseconds(a2+101));
  baseservo.writeMicroseconds(angleToMicroseconds(b+90));
}
void moveToPos(double x, double y, double z) {
  double b = atan2(y,x) * (180 / 3.1415); // base angle

  double l = sqrt(x*x + y*y); // x and y extension 

  double h = sqrt (l*l + z*z);

  double phi = atan(z/l) * (180 / 3.1415);

  double theta = acos((h/2)/75) * (180 / 3.1415);
  
  double a1 = phi + theta; // angle for first part of the arm
  double a2 = phi - theta; // angle for second part of the arm

  moveToAngle(b,a1,a2);
}
void setup() {
  baseservo.attach(BASESERVOPIN,460 ,2400);
  arm1servo.attach(ARM1SERVOPIN,460 ,2400);
  arm2servo.attach(ARM2SERVOPIN,460 ,2400);
  
  pinMode(BASEBUTTONPIN,INPUT);
  pinMode(ARM1BUTTONPIN,INPUT);
  pinMode(ARM2BUTTONPIN,INPUT);
  Serial.begin(115200);
  moveToPos(x,y,z);
}

void loop() {
  for (x=55; x<=130; x++) {
    moveToPos(x,y,z);
  }
  for (x=130; x>55; x--) {
    moveToPos(x,y,z);
  }
  int amount=1;
  long newPosition = myEnc.read();
  
  if (newPosition != oldPosition) {
    amount=newPosition-oldPosition;
    oldPosition = newPosition;
  }
  if (digitalRead(BASEBUTTONPIN) == HIGH && amount!=0) {
    x+=amount;
    moveToPos(x,y,z);
  }
  if (digitalRead(ARM1BUTTONPIN) == HIGH && amount!=0) {
    y+=amount;
    moveToPos(x,y,z);
  }
  if (digitalRead(ARM2BUTTONPIN) == HIGH && amount!=0) {
    z+=amount;
    moveToPos(x,y,z);
  }
}