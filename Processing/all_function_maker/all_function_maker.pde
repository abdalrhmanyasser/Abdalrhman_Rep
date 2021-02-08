import controlP5.*;
ControlP5 controlP5;
int state = 0;
RadioButton r;
float aPart = 1/40;
float bPart = 0;
float cPart = 0;
String firstString = "";
String secondString = "";
String thirdString = "";

void setup() {
  size(1000 ,600);
  controlP5 = new ControlP5(this);
  // CheckBox = multiple choice
  // RadioButton = single choice
  // Radio has been deprecated, should not be used anymore
  fill(0);
  r = controlP5.addRadioButton("radioButton")
         .setPosition(10,10)
         .setSize(30,40)
         .setColorForeground(color(205, 205, 205))
         .setColorBackground(color(255, 255, 255))
         .setColorActive(color(165, 165, 165))
         .setColorLabel(color(255))
         .setItemsPerRow(9)
         .setSpacingColumn(60)
         .addItem("Quadratic",1)
         .addItem("Cubic",2)
         .addItem("Linear",3)
         .addItem("absolute",4)
         .addItem("Square Root",5)
         .addItem("Cubic Root",6)
         .addItem("Sin",7)
         .addItem("Cos",8)
         .addItem("Tan",9)
         ;
  PFont font = createFont("arial",20);
  controlP5 = new ControlP5(this);
  controlP5.addTextfield("A")
         .setPosition(10,60)
         .setSize(90,40)
         .setColorLabel(color(255))
         .setColorForeground(color(140, 140, 140))
         .setColorBackground(color(140, 140, 140))
         .setColorActive(color(0, 0, 0))
         .setFont(createFont("arial",20))
         .setAutoClear(false)
         ;
  controlP5.addTextfield("B")
         .setPosition(110,60)
         .setColorLabel(color(255))
         .setColorForeground(color(140, 140, 140))
         .setColorBackground(color(140, 140, 140))
         .setColorActive(color(0, 0, 0))
         .setSize(90,40)
         .setFont(createFont("arial",20))
         .setAutoClear(false)
         ;
  controlP5.addTextfield("C")
         .setPosition(210,60)
         .setColorLabel(color(255))
         .setColorForeground(color(140, 140, 140))
         .setColorBackground(color(140, 140, 140))
         .setColorActive(color(0, 0, 0))
         .setSize(90,40)
         .setFont(createFont("arial",20))
         .setAutoClear(false)
         ;
  controlP5.addBang("send")
         .setPosition(310,60)
         .setSize(80,40)
         .setColorLabel(color(255))
         .setColorForeground(color(140, 140, 140))
         .setColorBackground(color(140, 140, 140))
         .setColorActive(color(0, 0, 0))
         .getCaptionLabel().align(ControlP5.CENTER, ControlP5.CENTER)
         ;
  controlP5.addBang("clear")
         .setPosition(400,60)
         .setSize(80,40)
         .setColorLabel(color(255))
         .setColorForeground(color(140, 140, 140))
         .setColorBackground(color(140, 140, 140))
         .setColorActive(color(0, 0, 0))
         .getCaptionLabel().align(ControlP5.CENTER, ControlP5.CENTER)
         ;
  textFont(font);
}



void draw() {
  background(255);
  float mousexmod = floor(mouseX/ 10) * 10;
  switch (state){
    case 0: // Quadratic was Chosen
      drawQuadraticfunc(aPart, bPart, cPart);
      findQuadraticPoint(aPart, bPart, cPart, mousexmod);
      break;
    case 1: // Cubic was Chosen
      drawCubicfunc(aPart, bPart, cPart);
      findCubicPoint(aPart, bPart, cPart, mousexmod);
      break;
    case 2: // Linear was Chosen
      drawLinearfunc(aPart, cPart);
      findLinearPoint(aPart, cPart, mousexmod);
      break;
    case 3: // Absolute was Chosen
      drawAbsolutefunc(aPart, bPart, cPart);
      findAbsolutePoint(aPart, bPart, cPart, mousexmod);
      break;
    case 4: // Square Root was Chosen
      drawSquareRootfunc(aPart, bPart, cPart);
      findSquareRootPoint(aPart, bPart, cPart, mousexmod);
      break;
    case 5: // Cubic Root was Chosen
      drawCubicRootfunc(aPart, bPart, cPart);
      findCubicRootPoint(aPart, bPart, cPart, mousexmod);
      break;
    case 6: // Sin was Chosen
      drawSinfunc(aPart, bPart, cPart);
      findSinPoint(aPart, bPart, cPart, mousexmod);
      break;
    case 7: // Cos was Chosen
      drawCosfunc(aPart, bPart, cPart);
      findCosPoint(aPart, bPart, cPart, mousexmod);
      break;
    case 8: // Tan was Chosen
      drawTanfunc(aPart, bPart, cPart);
      findTanPoint(aPart, bPart, cPart, mousexmod);
      break;
  }
  fill(0, 0, 0, 255);
  rect(0, 0, width, 140);
  stroke(0, 0, 0, 70);
  for (int i = 160; i < height; i+=40){
    line(0, i, width, i);
  }
  for (int i = 40; i < width; i+=40){
    line(i, 140, i, height);
  }
  stroke(0, 0, 0, 255);
  line(0, 360, width, 360);
  line(480, 140, 480, height);
  textSize(12);
  for (int i = -13; i < 12; i += 1){
    text(i, i*40 + width/2 - 15, height/2 + 75);
    line(i*40 + width/2 - 20, height/2 + 70, i*40 +width/2 - 20, height/2 + 50);
  }
  for (int i = 6; i > -7; i -= 1){
    if (i != 0){
      text(i, width/2 - 15, height/2 + 60 - i*40);
      line(width/2 - 10, height/2 + 20 - i*40, width/2 - 30, height/2 + 20 - i*40);
    }
  }
  line(width/2 - 10, height/2 + 20, width/2 - 30, height/2 + 20); 
  writedisc(state);
}

public void clear() {
  controlP5.get(Textfield.class,"A").clear();
  controlP5.get(Textfield.class,"B").clear();
  controlP5.get(Textfield.class,"C").clear();
  controlP5.get(Textfield.class,"A").submit();
  controlP5.get(Textfield.class,"B").submit();
  controlP5.get(Textfield.class,"C").submit();
}
void drawQuadraticfunc(float a, float b, float c){
  float y = 0;
  float py;
  float px;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  px = 0; py = 0;
  float xvertex = (-b)/(2*a);
  float yvertex = a*pow(xvertex, 2) + b*xvertex + c;
  stroke(0, 0, 0, 0);
  for(float x=-540; x<540; x+=.1){
    y = newheight - (a*pow(x, 2) + b*x + c);
    if (y > 140){
      line(px + newwidth, py, x + newwidth, y);
    }
    px = x;
    py = y;
    stroke(0);
  }
  firstString = "Vertex is : (" + xvertex / 40 + ", " + yvertex / 40 + ")";
  secondString = "axis of symetry is : " + (xvertex == 0 ? 0 : xvertex) / 40;
  
}
void findQuadraticPoint(float a, float b, float c, float d){
  stroke(0);
  strokeWeight(4);
  textSize(18);
  float y = 0;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  d -= newwidth;
  y = newheight - (a*pow(d, 2) + b*d + c);
  if (y > 140){
    fill(0);
    point(newwidth + d, y);
    text("(" + d / 40 + ", " + (height/2 + 60 - y) / 40 + ")", newwidth + d, y);
  }
  strokeWeight(1);
  textSize(12);
}

void drawCubicfunc(float a, float b, float c){
  float y = 0;
  float py;
  float px;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  a/=40;
  px = 0; py = 0;
  stroke(0, 0, 0, 0);
  for(float x=-540; x<540; x+=.1){
    y = newheight - (a*pow(x, 3) + b*x + c);
    if (y > 140){
      line(px + newwidth, py, x + newwidth, y);
    }
    px = x;
    py = y;
    stroke(0);
  }
}
void findCubicPoint(float a, float b, float c, float d){
  stroke(0);
  strokeWeight(4);
  textSize(18);
  float y = 0;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  d -= newwidth;
  a/=40;
  y = newheight - (a*pow(d, 3) + b*d + c);
  if (y > 140){
    fill(0);
    point(newwidth + d, y);
    text("(" + d / 40 + ", " + (height/2 + 60 - y) / 40 + ")", newwidth + d, y);
  }
  strokeWeight(1);
  textSize(12);
  firstString = "Vertex is : (0, " + c / 40 + ")";
  thirdString = "y intercept is : " + c / 40;
}
void drawLinearfunc(float a, float c){
  float y = 0;
  float py;
  float px;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  px = 0; py = 0;
  stroke(0, 0, 0, 0);
  for(float x=-540; x<540; x+=.1){
    y = newheight - (a*x*40 + c);
    if (y > 140){
      line(px + newwidth, py, x + newwidth, y);
    }
    px = x;
    py = y;
    stroke(0);
  }
  firstString = "Y intercept is : " + c / 40;
}
void findLinearPoint(float a, float c, float d){
  stroke(0);
  strokeWeight(4);
  textSize(18);
  float y = 0;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  d -= newwidth;
  y = newheight - (a*d*40 + c);
  if (y > 140){
    fill(0);
    point(newwidth + d, y);
    text("(" + d / 40 + ", " + (height/2 + 60 - y) / 40 + ")", newwidth + d, y);
  }
  strokeWeight(1);
  textSize(12);
}
void drawAbsolutefunc(float a, float b, float c){
  float y = 0;
  float py;
  float px;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  px = 0; py = 0;
  a*=40; b*=40;
  stroke(0, 0, 0, 0);
  for(float x=-540; x<540; x+=.1){
    y = newheight - (a*abs(x - b) + c);
    if (y > 140){
      line(px + newwidth, py, x + newwidth, y);
    }
    px = x;
    py = y;
    stroke(0);
  }
  firstString = "Vertex is : (" + b / 40 + ", " + c / 40 + ")";
  secondString = "axis of symetry is : " + (b == 0 ? 0 : b) / 40;
  thirdString = "y intercept is : " + (a * b + c) / 40;
}
void findAbsolutePoint(float a, float b, float c, float d){
  stroke(0);
  strokeWeight(4);
  textSize(18);
  float y = 0;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  d -= newwidth;
  a*=40; b*=40;
  y = newheight - (a*abs(d - b) + c);
  if (y > 140){
    fill(0);
    point(newwidth + d, y);
    text("(" + d / 40 + ", " + (height/2 + 60 - y) / 40 + ")", newwidth + d, y);
  }
  strokeWeight(1);
  textSize(12);
}
void drawSquareRootfunc(float a, float b, float c){
  float y = 0;
  float py;
  float px;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  px = 0; py = 0;
  stroke(0, 0, 0, 0);
  for(float x=b; x<540; x+=.1){
    y = newheight - (a*(sqrt(x/40 - b)*40)*40+c);
    if (y > 140){
      line(px + newwidth, py, x + newwidth, y);
    }
    px = x;
    py = y;
    stroke(0);
  }
}

void findSquareRootPoint(float a, float b, float c, float d){
  stroke(0);
  strokeWeight(4);
  textSize(18);
  float y = 0;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  d -= newwidth;
  println("a is " + a);
  println("b is " + b);
  println("c is " + c);
  println("c is " + d);
  y = newheight - (a*(sqrt(d/40 - b)*40)*40+c);
  if (y > 140){
    fill(0);
    point(newwidth + d, y);
    text("(" + d / 40 + ", " + (height/2 + 60 - y) / 40 + ")", newwidth + d, y);
  }
  strokeWeight(1);
  textSize(12);
}
void drawCubicRootfunc(float a, float b, float c){
  float y = 0;
  float py;
  float px;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  px = 0; py = 0;
  stroke(0, 0, 0, 0);
  for(float x=-540; x<540; x+=1){
    y = newheight - (a*((float) Math.cbrt(x/40 - b)*40)*40+c);
    if (y > 140){
      line(px + newwidth, py, x + newwidth, y);
    }
    px = x;
    py = y;
    stroke(0);
  }
  thirdString = "y intercept is : " + (a*((float) Math.cbrt(0/40 - b)*40)*40+c) / 40;
}

void findCubicRootPoint(float a, float b, float c, float d){
  stroke(0);
  strokeWeight(4);
  textSize(18);
  float y = 0;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  d -= newwidth;
  y = newheight - (a*((float) Math.cbrt(d/40 - b)*40)*40+c);
  if (y > 140){
    fill(0);
    point(newwidth + d, y);
    text("(" + d / 40 + ", " + (height/2 + 60 - y) / 40 + ")", newwidth + d, y);
  }
  strokeWeight(1);
  textSize(12);
}
void drawSinfunc(float a, float b, float c){
  float y = 0;
  float py;
  float px;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  px = 0; py = 0;
  stroke(0, 0, 0, 0);
  for(float x=-540; x<540; x+=1){
    y = newheight - (a*((float) sin(x/40 - b)*40)*40+c);
    if (y > 140){
      line(px + newwidth, py, x + newwidth, y);
    }
    px = x;
    py = y;
    stroke(0);
  }
  thirdString = "y intercept is : " + (a*((float) sin(0 - b)*40)*40+c) / 40;
}

void findSinPoint(float a, float b, float c, float d){
  stroke(0);
  strokeWeight(4);
  textSize(18);
  float y = 0;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  d -= newwidth;
  y = newheight - (a*((float) sin(d/40 - b)*40)*40+c);
  if (y > 140){
    fill(0);
    point(newwidth + d, y);
    text("(" + d / 40 + ", " + (height/2 + 60 - y) / 40 + ")", newwidth + d, y);
  }
  strokeWeight(1);
  textSize(12);
}
void drawCosfunc(float a, float b, float c){
  float y = 0;
  float py;
  float px;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  px = 0; py = 0;
  stroke(0, 0, 0, 0);
  for(float x=-540; x<540; x+=1){
    y = newheight - (a*((float) cos(x/40 - b)*40)*40+c);
    if (y > 140){
      line(px + newwidth, py, x + newwidth, y);
    }
    px = x;
    py = y;
    stroke(0);
  }
  thirdString = "y intercept is : " + (a*((float) cos(0 - b)*40)*40+c) / 40;
}

void findCosPoint(float a, float b, float c, float d){
  stroke(0);
  strokeWeight(4);
  textSize(18);
  float y = 0;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  d -= newwidth;
  y = newheight - (a*((float) cos(d/40 - b)*40)*40+c);
  if (y > 140){
    fill(0);
    point(newwidth + d, y);
    text("(" + d / 40 + ", " + (height/2 + 60 - y) / 40 + ")", newwidth + d, y);
  }
  strokeWeight(1);
  textSize(12);
}
void drawTanfunc(float a, float b, float c){
  float y = 0;
  float py;
  float px;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  px = 0; py = 0;
  stroke(0, 0, 0, 0);
  for(float x=-540; x<540; x+=1){
    y = newheight - (a*((float) tan(x/40 - b)*40)*40+c);
    if (y < width){
      line(px + newwidth, py, x + newwidth, y);
    }
    px = x;
    py = y;
    stroke(0);
  }
  thirdString = "y intercept is : " + (a*((float) tan(0 - b)*40)*40+c) / 40;
}

void findTanPoint(float a, float b, float c, float d){
  stroke(0);
  strokeWeight(4);
  textSize(18);
  float y = 0;
  float newheight = height/2 + 60;
  float newwidth = width/2 - 20;
  d -= newwidth;
  y = newheight - (a*((float) tan(d/40 - b)*40)*40+c);
  if (y > 140 && y < width){
    fill(0);
    point(newwidth + d, y);
    text("(" + d / 40 + ", " + (height/2 + 60 - y) / 40 + ")", newwidth + d, y);
  }
  strokeWeight(1);
  textSize(12);
}
void writedisc(int state){
  switch (state){
    case 0: // Quadratic was Chosen
      fill(255, 127.5);
      rect(490, 60, 10+(textWidth(firstString) >= textWidth(secondString) ? textWidth(firstString) : textWidth(secondString)), 40);
      fill(255);
      text(firstString , 495, 75);
      text(secondString, 495, 93);
      break;
    case 1: // Cubic was Chosen
      fill(255, 127.5);
      float num = (textWidth(firstString) >= textWidth(thirdString) ? textWidth(firstString) : textWidth(thirdString));
      rect(490, 60, 10+num, 40);
      fill(255);
      text(firstString , 495, 75);
      text(thirdString, 495, 93);
      break;
    case 2: // Linear was Chosen
      fill(255, 127.5);
      rect(490, 60, 10+(textWidth(firstString)), 22);
      fill(255);
      text(firstString , 495, 75);
      break;
    case 3: // Absolute was Chosen
      fill(255, 127.5);
      float num1 = (textWidth(firstString) >= textWidth(secondString) ? textWidth(firstString) : textWidth(secondString));
      rect(490, 60, 10+(num1 > textWidth(thirdString) ? num1 : textWidth(thirdString)), 60);
      fill(255);
      text(firstString , 495, 75);
      text(secondString, 495, 93);
      text(thirdString, 495, 111);
      break;
    case 5: // Cubic Root was Chosen
      fill(255, 127.5);
      rect(490, 60, 10+textWidth(thirdString), 20);
      fill(255);
      text(thirdString , 495, 75);
      break;
    case 6: // Sin was Chosen
      fill(255, 127.5);
      rect(490, 60, 10+textWidth(thirdString), 20);
      fill(255);
      text(thirdString , 495, 75);
      break;
    case 7: // Cos was Chosen
      fill(255, 127.5);
      rect(490, 60, 10+textWidth(thirdString), 20);
      fill(255);
      text(thirdString , 495, 75);
      break;
    case 8: // Tan was Chosen
      fill(255, 127.5);
      rect(490, 60, 10+textWidth(thirdString), 20);
      fill(255);
      text(thirdString , 495, 75);
      break;
  }
}


void controlEvent(ControlEvent theEvent) {
  println(theEvent.getName());
  if(theEvent.isGroup() && theEvent.name().equals("radioButton")) {
    for (int i = 0; i < 9;i++){
      if (theEvent.arrayValue()[i] == 1){
        println(i);
        state = i;
      }
    }
  }
  else if(theEvent.isAssignableFrom(Textfield.class)) {
    if (theEvent.getName() == "A"){
        aPart = !Float.isNaN(float(theEvent.getStringValue())) ? (float(theEvent.getStringValue())) / 40 : 0;
        println(aPart);
    }
    else if (theEvent.getName() == "B"){
        bPart = !Float.isNaN(float(theEvent.getStringValue())) ? (float(theEvent.getStringValue())) : 0;
        println(bPart);
    }
    else if (theEvent.getName() == "C"){
        cPart = !Float.isNaN(float(theEvent.getStringValue())) ? (float(theEvent.getStringValue())) * 40: 0;
        println(cPart);
    }
  }
  else if(theEvent.name().equals("send")){
      controlP5.get(Textfield.class,"A").submit();
      controlP5.get(Textfield.class,"B").submit();
      controlP5.get(Textfield.class,"C").submit();
  }
}
