float R = 500/2;
float M = 10;
float g = 10;
float now = millis();
float prev = millis();
float delta = now - prev;
float theta = PI/4;
PVector blob;
float Velocity = 0;
float acc = 0;
void setup(){
  size(500, 500);
  blob = new PVector(R * cos(theta), R * sin(theta));
}
int sign(float x){
  if (x >= 0){
    return 1;
  }else{
    return -1;
  }
}

void draw(){
  background(255);
  now = millis()*0.01;
  delta = now - prev;
  translate(width/2, 0);
  float angOfR = blob.heading()+PI/2*sign(theta);
  if (blob.y > 0) {
    theta = atan(blob.x / blob.y);
  }
  PVector Restoring = new PVector(1, 1).setMag(-M*g*sin(theta)).setHeading(angOfR);
  line(0, 0, blob.x, blob.y);
  circle(blob.x, blob.y, 20);
  acc = Restoring.mag()*sign(theta);
  Velocity+=acc;
  blob.x += Velocity*cos(blob.heading()+PI/2)*delta;
  blob.y += Velocity*sin(blob.heading()+PI/2)*delta;
  prev = now;
}
