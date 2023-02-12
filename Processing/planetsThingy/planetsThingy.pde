import controlP5.*;
import java.util.*;
PVector[][] trails = new PVector[20][200];
int maxTrailLength = 200;

boolean velocityMode = false;
ControlP5 cp5;
Planet[] planets;
float Sim_speed = 1;
float SizeOfExit;
float sizeOfPixls = 0;
float prev = 0;
float delta = 0;
float now = millis();
int numOfPlanets = 0;
boolean simStarted = false;
float Velocity = 100;
float Mass = 500;
float Radius = 70;
float G = 2.4;
boolean Movable = true;
CheckBox checkbox;

class Planet {
  float mass, radius;
  PVector velocity, pos;
  boolean movable;
  int index = 0;
  Planet(float _mass, float _x, float _y, PVector _velocity, float _radius, boolean _movable, int _index) {
    mass = _mass;
    index = _index;
    radius = _radius;
    velocity = _velocity;
    pos = new PVector(_x, _y);
    movable = _movable;
  }

  void update() {
    if (movable == true) {
      pos.x += velocity.x*delta*Sim_speed;
      pos.y += velocity.y*delta*Sim_speed;
    }
  }
}
void setup() {
  fullScreen();
  smooth();
  planets = new Planet[20];
  sizeOfPixls = width*0.1;
  SizeOfExit = sizeOfPixls*.8;
  stroke(255, 0, 0);
  strokeWeight(2);
  frameRate(60);
  printArray(trails);

  cp5 = new ControlP5(this);

  // create another slider with tick marks, now without
  // default value, the initial value will be set according to
  // the value of variable sliderTicks2 then.
  cp5.addSlider("Velocity")
    .setPosition(sizeOfPixls*.6, sizeOfPixls*.1)
    .setSize(int(sizeOfPixls*1.4), int(sizeOfPixls*.4))
    .setRange(0, 255)
    ;
  cp5.addSlider("Mass")
    .setPosition(sizeOfPixls*2.1, sizeOfPixls*.1)
    .setSize(int(sizeOfPixls*1.4), int(sizeOfPixls*.4))
    .setRange(50, 10000)
    ;
  cp5.addSlider("Radius")
    .setPosition(sizeOfPixls*3.6, sizeOfPixls*.1)
    .setSize(int(sizeOfPixls*1.4), int(sizeOfPixls*.4))
    .setRange(1, 100)
    ;
  cp5.addSlider("Sim_Speed")
    .setPosition(sizeOfPixls*5.1, sizeOfPixls*.1)
    .setSize(int(sizeOfPixls*1.4), int(sizeOfPixls*.4))
    .setValue(5)
    .setRange(1, 10)
    ;
  checkbox = cp5.addCheckBox("Movable")
    .setPosition(sizeOfPixls*7.1, sizeOfPixls*.1)
    .setColorForeground(color(120))
    .setColorActive(color(255))
    .setColorLabel(color(255))
    .setSize(int(sizeOfPixls*.4), int(sizeOfPixls*.4))
    .addItem("Moveable", 0)
    .activate(0)
    ;
  cp5.addButton("Clear")
    .setPosition(sizeOfPixls*6.6, sizeOfPixls*.1)
    .setSize(int(sizeOfPixls*.4), int(sizeOfPixls*.4))
    ;
  cp5.getController("Velocity").getCaptionLabel().align(ControlP5.LEFT, ControlP5.BOTTOM_OUTSIDE).setPaddingX(0);
  cp5.getController("Mass").getCaptionLabel().align(ControlP5.LEFT, ControlP5.BOTTOM_OUTSIDE).setPaddingX(0);
  cp5.getController("Radius").getCaptionLabel().align(ControlP5.LEFT, ControlP5.BOTTOM_OUTSIDE).setPaddingX(0);
  cp5.getController("Sim_Speed").getCaptionLabel().align(ControlP5.LEFT, ControlP5.BOTTOM_OUTSIDE).setPaddingX(0);
}
public void Clear() {
  planets = new Planet[20];
  numOfPlanets = 0;
}
void Sim_Speed(float value) {
  Sim_speed = value;
}
void draw() {
  now = millis()*.01;
  delta = now - prev;
  fill(177);
  background(0);
  for (int j = 0; j < numOfPlanets; j++) {
    fill(177);
    circle(planets[j].pos.x, planets[j].pos.y, planets[j].radius);
  }
  if (velocityMode) {
    line(planets[numOfPlanets-1].pos.x, planets[numOfPlanets-1].pos.y, mouseX, mouseY);
  }
  if (simStarted) {
    simulate();
  }
  fill(0);
  stroke(255);
  rect(width-(SizeOfExit), 0, SizeOfExit, SizeOfExit*.5);
  line(width-SizeOfExit*.8, SizeOfExit*.1, width-SizeOfExit*.2, SizeOfExit*.4);
  line(width-SizeOfExit*.2, SizeOfExit*.1, width-SizeOfExit*.8, SizeOfExit*.4);

  float sizeOfPlay = sizeOfPixls * .5;
  rect(0, 0, sizeOfPlay, sizeOfPlay);
  line(sizeOfPlay*.2, sizeOfPlay*.2, sizeOfPlay*.2, sizeOfPlay*.8);
  line(sizeOfPlay*.2, sizeOfPlay*.2, sizeOfPlay*.8, sizeOfPlay*.5);
  line(sizeOfPlay*.2, sizeOfPlay*.8, sizeOfPlay*.8, sizeOfPlay*.5);
  for (int j = 0; j < trails.length; j++) {
    if (trails[j].length >= 2) {
      PVector currPoint, lastPoint = trails[j][0];
      for (int i = 0; i < trails[j].length; i++) {
          currPoint = trails[j][i];
        if (!(currPoint == null)) {
          stroke(255, map(i, 0, trails[j].length, 255, 0));
          line(lastPoint.x, lastPoint.y, currPoint.x, currPoint.y);
          lastPoint = currPoint;
        }
      }
    }
  }
  prev = now;
}
void controlEvent(ControlEvent theEvent) {
  if (theEvent.isFrom(checkbox)) {
    int n = (int)checkbox.getArrayValue()[0];
    if (n==1) {
      Movable = true;
    } else {
      Movable = false;
    }
  }
}
void simulate() {
  for (int j = 0; j < numOfPlanets; j++) {
    PVector Force = new PVector(0, 0);
    for (int i = 0; i < numOfPlanets; i++) {
      if (i != j) {
        float mag = G*((planets[j].mass + planets[i].mass) / dist(planets[j].pos.x, planets[j].pos.y, planets[i].pos.x, planets[i].pos.y));
        Force = new PVector(planets[j].pos.x - planets[i].pos.x, planets[j].pos.y - planets[i].pos.y);
        Force.normalize();
        Force.setMag(mag);
      }
    }
    planets[j].velocity.x -= Force.x/planets[j].mass;
    planets[j].velocity.y -= Force.y/planets[j].mass;
    planets[j].update();

    PVector p = new PVector(planets[j].pos.x, planets[j].pos.y);
    trails[planets[j].index] = (PVector[])splice(trails[planets[j].index], p, 0);
    // If trail is too 'long' remove the oldest points
    while (trails[planets[j].index].length > maxTrailLength)
      trails[planets[j].index] = (PVector[])(subset(trails[planets[j].index], 0, trails[planets[j].index].length-1));
  }
}
void mouseClicked() {
  if (mouseY < sizeOfPixls*1.2) {
    if (mouseX > width-SizeOfExit && mouseY < SizeOfExit*.5) {
      exit();
    } else if (mouseX < sizeOfPixls*.5 && mouseY < sizeOfPixls*.5 && velocityMode != true) {
      simStarted = true;
    }
  } else {
    if (!velocityMode) {
      simStarted = false;
      velocityMode = true;
      Planet planet;
      planet = new Planet(10, mouseX, mouseY, new PVector(0, 0), 10, Movable, numOfPlanets);
      planets[numOfPlanets] = planet;
      planets[numOfPlanets].mass = Mass;
      planets[numOfPlanets].radius = Radius;
      numOfPlanets++;
    } else {
      planets[numOfPlanets-1].velocity = new PVector(mouseX, mouseY).sub(planets[numOfPlanets-1].pos);
      planets[numOfPlanets-1].velocity.setMag(Velocity/ 63.75);

      velocityMode = false;
    }
  }
}
