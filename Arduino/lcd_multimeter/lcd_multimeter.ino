
void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(5, OUTPUT);
  pinMode(7, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  float vvalue = analogRead(A0);
  float gndvalue = analogRead(A1);
  analogWrite(5, (((vvalue - gndvalue) / 204.6) / 5) * 255);
  Serial.println((((vvalue - gndvalue) / 204.6) / 5) * 5);
  digitalWrite(7, HIGH);
  delay(200);
}
