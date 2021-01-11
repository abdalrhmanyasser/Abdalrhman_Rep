
#include <LiquidCrystal.h>
const int rs = 12, en = 13, d4 = 8, d5 = 9, d6 = 10, d7 = 11;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
void setup() {
  lcd.begin(16, 2);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  float vvalue = analogRead(A0);
  float gndvalue = analogRead(A1);
  lcd.setCursor(0, 0);
  lcd.clear();
  lcd.print("Voltage : " + String(vvalue - gndvalue));
  delay(100);
}
