import java.awt.Color;
float m1 = 1;
float m2 = 1;
float x1;
float x2;
float y1;
float y2;
float r1 = 2;
float r2 = 2;
float[] x1arr;
float[] x2arr;
float[] y1arr;
float[] y2arr;
float g = 4.9/(60*60);
float x1_acc = 0;
float y1_acc = 0;
float x2_acc = 0;
float y2_acc = 0;
float x1_vel, x2_vel, y1_vel, y2_vel = 0;
float a1 = HALF_PI;
float a2 = HALF_PI;
float a1_v = 0;
float a2_v = 0;
float i = 0;
int SizeOfColor = 1;
PGraphics canvas;
float px2 = -1; // previous position of second pendulum sphere - x offset
float py2 = -1; // previos position of second pendulum sphere - y offset
float cx, cy; //centre of x and y for background

void setup() {
  size(900, 600);
  colorMode(HSB);
  cx = width/2;
  cy = 200;
  canvas = createGraphics(width, height);
  canvas.beginDraw();
  canvas.background(255);
  canvas.endDraw();
}


void draw() {

  push();
  background(255);
  imageMode(CORNER);
  image(canvas, 0, 0, width, height);
  // numerators are moduled
  float num1 = -g * (2 * m1 + m2) * sin(a1);
  float num2 = -m2 * g * sin(a1-2*a2);
  float num3 = -2*sin(a1-a2)*m2;
  float num4 = a2_v*a2_v*r2+a1_v*a1_v*r1*cos(a1-a2);
  float den = r1 * (2*m1+m2-m2*cos(2*a1-2*a2));
  float a1_a = (num1 + num2 + num3*num4) / den;

  num1 = 2 * sin(a1-a2);
  num2 = (a1_v*a1_v*r1*(m1+m2));
  num3 = g * (m1 + m2) * cos(a1);
  num4 = a2_v*a2_v*r2*m2*cos(a1-a2);
  den = r2 * (2*m1+m2-m2*cos(2*a1-2*a2));
  float a2_a = (num1*(num2+num3+num4)) / den;

  //UPDATING THE X AND THE Y

  x1 = r1 * sin(a1);
  y1 = r1 * cos(a1);

  x2 = x1 + r2 * sin(a2);
  y2 = y1 + r2 * cos(a2);

  //UPDATE VELOCITIES AND ACCESLERATION
  a1_v += a1_a;
  a2_v += a2_a;
  a1 += a1_v;
  a2 += a2_v;



  translate(cx, cy);
  stroke(0);
  strokeWeight(2);


  //DRAWING THE SHAPES


  line(0, 0, x1 * 100, y1 * 100);
  fill(0);
  ellipse(x1 * 100, y1 * 100, m1 * 10, m1 * 10);

  line(x1 * 100, y1 * 100, x2 * 100, y2 * 100);
  fill(0);
  ellipse(x2 * 100, y2 * 100, m2 * 10, m2 * 10);

  // as momentum increases  , slowly pendulum comes to rest
  a1_v *= 1.00000001; // for drag
  a2_v *= 1.00000001; // for drag




  canvas.beginDraw();
  //canvas.background(0, 1);
  canvas.translate(cx, cy);
  canvas.strokeWeight(SizeOfColor);
  canvas.stroke(3);
  if (i >= 360) {
    i = 0;
  }
  i+= 0.3;
  colorMode(HSB);
  color c = color(i, 255, 255);
  canvas.stroke(c);
  if (frameCount > 1) {
    canvas.line(px2 * 100, py2 * 100, x2 * 100, y2 * 100);
  }
  canvas.endDraw();
  pop();
  px2 = x2;
  py2 = y2;
}
