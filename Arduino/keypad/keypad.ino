#include <Keypad.h>
#include <LiquidCrystal.h>

const int rs = 12, en = 13, d4 = 8, d5 = 9, d6 = 10, d7 = 11;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

const byte ROWS = 4; 
const byte COLS = 4; 

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {4, 5, 6, 7}; 
byte colPins[COLS] = {A1, A0, 2, 3}; 

Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

void setup(){  
  lcd.begin(16, 2);
  Serial.begin(9600);
  Serial.println("ah");
}
int indexx = 0;
int indexy = 0;
void loop(){
  char customKey = customKeypad.getKey();
  
  if (customKey){  
    Serial.println(customKey);
    if(customKey != '*' &&customKey != '#'){
      lcd.setCursor(indexx, indexy);
      if (indexx >= 15 && indexy != 1){
        indexy++;
        indexx = -1;
      }else if (indexx >= 15 && indexy == 1){
        indexx = 14;
      }
      lcd.print(customKey);
      indexx++;
    }else if(customKey == '#'){
      lcd.setCursor(indexx, indexy);
      lcd.print(' ');
      if (indexx == 16){
        indexy++;
        indexx = -1;
      }
      indexx++;
    }else if (indexx != 0 || indexy == 1 ){
      if (indexx == 0 && indexy == 1){
        lcd.setCursor(0, 1);
        lcd.print(' ');
        lcd.setCursor(15, 0);
        lcd.print(' ');
        lcd.setCursor(15, 0);
        indexy--;
        indexx = 16;
      }else if (indexx <= 15 && indexy != 1){
        lcd.setCursor((indexx - 1), indexy);
        lcd.print(' ');
        lcd.setCursor((indexx - 1), indexy);
      }else if (indexx <= 15 && indexy != 0){
        lcd.setCursor(indexx, indexy);
        lcd.print(' ');
        lcd.setCursor(indexx, indexy);
      }else {
        lcd.setCursor(15 , indexy);
        lcd.print(' ');
        lcd.setCursor(14 , indexy);
        indexx = 14;
      }
      indexx--;
    }
    lcd.cursor();
  }
}
