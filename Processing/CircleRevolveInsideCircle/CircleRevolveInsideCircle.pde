import java.awt.Color;
PGraphics canvas;
int xMoved = 0;
int[] ratio = {400,120};
int[] circle1 = {300, 300, (ratio[0])};
float x = (circle1[1]+circle1[2]/2) - (ratio[1]/2);
float y = 300;
float RevsInnerCircle;
float RevsBiggerCircle;
int circle2Size = ratio[1];
float distanceFromCenterC2 = 0.75;
boolean drawCircle = true;

void setup() {
  size(600, 600);
  canvas = createGraphics(width, height);
  canvas.beginDraw();
  canvas.strokeWeight(4);
  canvas.endDraw();
}

void draw(){

  for (int i = 0; i < 20;i++){
    xMoved+=2;
    RevsInnerCircle = xMoved/(2*PI*circle2Size);
    
    RevsBiggerCircle = xMoved/(2*PI*circle1[2]);
    
    x = circle1[0]+((circle1[2]/2)-(circle2Size/2))*cos(RevsBiggerCircle);
    y = circle1[0]+((circle1[2]/2)-(circle2Size/2))*sin(RevsBiggerCircle);
    
    strokeWeight(2);
    if (drawCircle){
    background(177);
  }
    ellipse(circle1[0], circle1[1], circle1[2], circle1[2]);
    if (drawCircle){
      strokeWeight(1);
      ellipse(x, y, circle2Size, circle2Size);
    }
    line(x, y, x+(circle2Size/2*distanceFromCenterC2)*cos(-RevsInnerCircle), y+(circle2Size/2*distanceFromCenterC2)*sin(-RevsInnerCircle));
    strokeWeight(10);
    point(x, y);
    point(circle1[0], circle1[1]);
    canvas.beginDraw();
    canvas.stroke(0);
    canvas.point(x+(circle2Size/2*distanceFromCenterC2)*cos(-RevsInnerCircle), y+(circle2Size/2*distanceFromCenterC2)*sin(-RevsInnerCircle));
    canvas.endDraw();
  }
  frameRate(60);
  println(frameRate);
  image(canvas, 0, 0);
}
void keyPressed() {
    if (key == 'b' || key == 'B') {
      drawCircle=!drawCircle;
    }
  }
