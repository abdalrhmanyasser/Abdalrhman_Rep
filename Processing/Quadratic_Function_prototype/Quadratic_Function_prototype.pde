import controlP5.*;

ControlP5 cp5;

String[] textfieldNames = {"a", "B" , "k"};
float aPart = .1;
float kPart = 0;
float bPart = 0;
void setup() {
  size(500,500);
  println(pow(1, 2));

  PFont font = createFont("arial",20);

  cp5 = new ControlP5(this);

  int x = 20;
  int spacing = (width/8)*2 + 30;
  for(String name: textfieldNames){
    cp5.addTextfield(name)
       .setPosition(x,20)
       .setSize((width/8)*2,40)
       .setFont(font)
       .setFocus(false)
       .setColor(color(255, 255,255))
       ;
     x += spacing;
  }

  textFont(font);
}

void draw() {
  background(255);
  rect(0, 0, width, 100);
  textSize(20);
  for (int x =0; x<height; x+=20){
    stroke(0, 0, 0, 60);
    line(x + 10, 0, x + 10, height);
  }
  stroke(0);
  fill(0, 102, 153);
  text("y", 250, 150);
  line(250, 0, 250, height);
  fill(0, 102, 153);
  text("x", width - 50, height - 40);
  line(0, height - 25, width, height - 25);
  for (int i = 0; i < 12; i += 1){
    textSize(12);
    text(i, i*20 + 250, height - 10);
    line(i*20 + 250, height - 20, i*20 + 250, height - 30);
  }
  for (int i = 0; i < 12; i += 1){
    textSize(12);
    text(i, 250, height - i*40 - 10);
    line(i*20 + 250, height - 20, i*20 + 250, height - 30);
  }
  for (int i = 0; i > -13; i -= 1){
    textSize(12);
    text(i, i*20 + 250, height - 10);
    line(i*20 + 250, height - 20, i*20 + 250, height - 30);
  }
  for (int t =0; t<height; t+=40){
    stroke(0, 0, 0, 60);
    line(0, t - 5, width, t -5);
  }
  text("Vertex = (" + bPart  / 20+ ", " + kPart / 40 + " )" , 400, 120 );
  
  
  
  
   strokeWeight(1);
   stroke(0);
  quadraticPoints(aPart, bPart, kPart + 25, 1);
   strokeWeight(1);
   stroke(255, 0, 0, 50);
  quadraticPoints(.1, 0, 0 + 25, 2);
}

void controlEvent(ControlEvent theEvent) {
  if(theEvent.isAssignableFrom(Textfield.class)) {
    if (theEvent.getName() == "a"){
        aPart = float(theEvent.getStringValue()) / 10;
    }
    else if (theEvent.getName() == "k"){
        kPart = float(theEvent.getStringValue()) * 40;
    }
    else{
        bPart = float(theEvent.getStringValue()) * 20;
      
      
    }
  }
}

void quadraticPoints (float a, float b, float c, int j){
  float y = 0;
  float py;
  float px;
   px = 0; py = 0;
  
   stroke(0, 0, 0, 0);
  for(float x=-500; x<500; x+=.01){
    y = height - ( (a*pow((x-b), 2)) + c );
    line(px + width/2, py, x + width /2, y);
    px = x;
    py = y;
    if( j == 1){
       stroke(0);
    }
    if( j == 2){
       stroke(255, 0, 0, 50);
    }
  }
}
