int index = 0;
bool states = true;
// Example 2 - Receive with an end-marker
const byte numChars = 32;
char receivedChars[numChars];   // an array to store the received data
char on[3] = {'O', 'N', '\n'};
char off[4] = {'O', 'F', 'F', '\n'};
boolean newData = false;
long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}
void setup() {
    Serial.begin(9600);
    Serial.println("<Arduino is ready>");
    pinMode(9, OUTPUT);
      pinMode(12, OUTPUT);
    pinMode(11, OUTPUT);
    pinMode(A0, INPUT);
    pinMode(A1, INPUT);
}
void change(){
  if (index == 0){
    digitalWrite(9, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
  }
  else if(index == 1){
    digitalWrite(9, LOW);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
  }
  else if(index == 2){
    digitalWrite(9, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    index = -1;
  }
}
void loop() {
    recvWithEndMarker();
    showNewData();
    if (analogRead(A0) < 50 && analogRead(A1) < 50){
    }else if (analogRead(A0) < 10){
      states = false;
    }else if (analogRead(A1) < 10){
      states = true;
    }
    if (states){
      change();
      index++;
    }else if (states == false){
      float reading = 0.01723 * readUltrasonicDistance(2, 3);
    Serial.println(0.01723 * readUltrasonicDistance(2, 3));
      if (reading < 20){
        digitalWrite(9, HIGH);
        digitalWrite(12, LOW);
        digitalWrite(11, LOW);
      }else if (reading < 30){
        digitalWrite(9, LOW);
        digitalWrite(12, HIGH);
        digitalWrite(11, LOW);
      }else if (reading < 40){
        digitalWrite(9, LOW);
        digitalWrite(12, LOW);
        digitalWrite(11, HIGH);
      }else if (reading < 50){
        digitalWrite(9, HIGH);
        digitalWrite(12, HIGH);
        digitalWrite(11, HIGH);
      } 
    }
    delay(333);
}

void recvWithEndMarker() {
    static byte ndx = 0;
    char endMarker = '\n';
    char rc;
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();
        if (rc != endMarker) {
            receivedChars[ndx] = rc;
            ndx++;
            if (ndx >= numChars) {
                ndx = numChars - 1;
            }
        }
        else {
            receivedChars[ndx] = '\0'; // terminate the string
            ndx = 0;
            newData = true;
        }
    }
}

void showNewData() {
    if (newData == true) {
      Serial.print("This just in ... ");
      Serial.println(receivedChars);
      if(strcmp(receivedChars, "cycle") == 0){
        states = true;
      }else if(strcmp(receivedChars, "sensor") == 0){
        states = false;
      }
      newData = false;
    }
}
