#include <IRremote.h>

// Define sensor pin
const int RECV_PIN = 9;

// Define IR Receiver and Results Objects`
IRrecv irrecv(RECV_PIN);
decode_results results;
const int A = 2, B = 3, C = 4, D = 5, E = 6, F = 7, G = 8;
bool Abit = false, Bbit = false, Cbit = false, Dbit = false, Ebit = false, Fbit = false, Gbit = false;
const int led1 = 10, led2 = 11, led3 = 12, led4 = 13;

void setup() {
  Serial.begin(9600);
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(G, OUTPUT);
  
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);

  pinMode(A0, INPUT);
  // Enable the IR Receiver
  irrecv.enableIRIn();
}
int num = 0;
bool ppinmode = false;
bool npinmode = false;
void loop() {
  // put your main code here, to run repeatedly:
  checkpin();
  setdigit();
  int frstbit = num % 2;
  int scndbit = num/2 % 2;
  int thrdbit = int(num/2)/2 % 2;
  int frthbit = int(int(num/2)/2)/2 % 2;
  
  digitalWrite(led1, frstbit);
  digitalWrite(led2, scndbit);
  digitalWrite(led3, thrdbit);
  digitalWrite(led4, frthbit);
  if (irrecv.decode(&results)){
    // Print Code in HEX
        if (results.value == 16738455){// 0
          num = 0;
        }else if (results.value == 16724175){// 1
          num = 1;
        }else if (results.value == 16718055){// 2
          num = 2;
        }else if (results.value == 16743045){// 3
          num = 3;
        }else if (results.value == 16716015){// 4
          num = 4;
        }else if (results.value == 16726215){// 5
          num = 5;
        }else if (results.value == 16734885){// 6
          num = 6;
        }else if (results.value == 16728765){// 7
          num = 7;
        }else if (results.value == 16730805){// 8
          num = 8;
        }else if (results.value == 16732845){// 9
          num = 9;
        }else if (results.value == 16712445){// +
          num++;
        }else if (results.value == 16750695){// -
          num--;
        }
        Serial.println(results.value);
        irrecv.resume();
  }
}
void setdigit(){
  if (num == 0){
    Abit = false;
    Bbit = true;
    Cbit = true;
    Dbit = true;
    Ebit = true;
    Fbit = true;
    Gbit = true;
  }else if (num == 1){
    Abit = false;
    Bbit = false;
    Cbit = false;
    Dbit = true;
    Ebit = false;
    Fbit = false;
    Gbit = true;
  }else if (num == 2){
    Abit = true;
    Bbit = false;
    Cbit = true;
    Dbit = true;
    Ebit = true;
    Fbit = true;
    Gbit = false;
  }else if (num == 3){
    Abit = true;
    Bbit = false;
    Cbit = true;
    Dbit = true;
    Ebit = false;
    Fbit = true;
    Gbit = true;
  }else if (num == 4){
    Abit = true;
    Bbit = true;
    Cbit = false;
    Dbit = true;
    Ebit = false;
    Fbit = false;
    Gbit = true;
  }else if (num == 5){
    Abit = true;
    Bbit = true;
    Cbit = true;
    Dbit = false;
    Ebit = false;
    Fbit = true;
    Gbit = true;
  }else if (num == 6){
    Abit = true;
    Bbit = true;
    Cbit = true;
    Dbit = false;
    Ebit = true;
    Fbit = true;
    Gbit = true;
  }else if (num == 7){
    Abit = false;
    Bbit = true;
    Cbit = true;
    Dbit = true;
    Ebit = false;
    Fbit = false;
    Gbit = true;
  }else if (num == 8){
    Abit = true;
    Bbit = true;
    Cbit = true;
    Dbit = true;
    Ebit = true;
    Fbit = true;
    Gbit = true;
  }else if (num == 9){
    Abit = true;
    Bbit = true;
    Cbit = true;
    Dbit = true;
    Ebit = false;
    Fbit = true;
    Gbit = true;
  }else if (num == 10){
    Abit = true;
    Bbit = true;
    Cbit = true;
    Dbit = true;
    Ebit = true;
    Fbit = false;
    Gbit = true;
  }else if (num == 11){
    Abit = true;
    Bbit = true;
    Cbit = false;
    Dbit = false;
    Ebit = true;
    Fbit = true;
    Gbit = true;
  }else if (num == 12){
    Abit = false;
    Bbit = true;
    Cbit = true;
    Dbit = false;
    Ebit = true;
    Fbit = true;
    Gbit = false;
  }else if (num == 13){
    Abit = true;
    Bbit = false;
    Cbit = false;
    Dbit = true;
    Ebit = true;
    Fbit = true;
    Gbit = true;
  }else if (num == 14){
    Abit = true;
    Bbit = true;
    Cbit = true;
    Dbit = false;
    Ebit = true;
    Fbit = true;
    Gbit = false;
  }else if (num == 15){
    Abit = true;
    Bbit = true;
    Cbit = true;
    Dbit = false;
    Ebit = true;
    Fbit = false;
    Gbit = false;
  }
  digitalWrite(A, Abit);
  digitalWrite(B, Bbit);
  digitalWrite(C, Cbit);
  digitalWrite(D, Dbit);
  digitalWrite(E, Ebit);
  digitalWrite(F, Fbit);
  digitalWrite(G, Gbit);
}


void checkpin(){
  npinmode = analogRead(A0) == 1023;
  if (ppinmode == false && ppinmode != npinmode){
    num++;
    delay(200);
  }
  if(num == 16 || num == -1){
    num = 0;
  }
  ppinmode = npinmode; 
}
