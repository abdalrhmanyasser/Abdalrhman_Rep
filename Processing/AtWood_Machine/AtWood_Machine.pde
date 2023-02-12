String status = "Float";
float v = 0;
float a = 0;
float l1 = 300;
float l2 = 300;
float m1 = 5.1;
float m2 = 5;
int sizeOfBox = 5;
long lastTime;
class Button {
  float x, y, WIDTH, HEIGHT;
  String text;
  Button(float _x, float _y, float _WIDTH, float _HEIGHT, String _text) {
    x = _x;
    y = _y;
    WIDTH = _WIDTH;
    HEIGHT = _HEIGHT;
    text = _text;
  }
  void update() {
    fill(0);
    rect(x, y, WIDTH, HEIGHT);
    fill(255);
    textSize(16);
    text(text, (x+(WIDTH/2))-(textWidth(text)/2), (y+(HEIGHT/2)));
  }
  boolean checkClick(float _x, float _y) {
    if ((x < _x && y < _y) && (x+WIDTH > _x && y+HEIGHT > _y)) {
      return true;
    } else {
      return false;
    }
  }
}
Button b1 = new Button( 10.0, 10.0, 112.5, 80.0, "Float");
Button b2 = new Button(132.5, 10.0, 112.5, 80.0, "Ground");
Button b3 = new Button(255.0, 10.0, 112.5, 80.0, "Slope");
Button b4 = new Button(377.5, 10.0, 112.5, 80.0, "both Slope");
void setup() {
  size(900, 700);
  background(220, 220, 255);
  frameRate(60);
}

void draw() {
  background(150, 150, 255);
  fill(60, 60, 255, 177);
  rect(0, 0, width, 100);
  b1.update();
  b2.update();
  b3.update();
  b4.update();
  stroke(4);
  if (status != "") {
    switch (status) {
    case "Float":
      if (l1 > 0 && l2 > 0) {
        a = (((m1*10)-(m2*10))/(m1+m2))/(60);
        v+=a;
        a=0;
        l1 = l1 + v;
        l2 = l2 - v;
      }
      stroke(0);
      strokeWeight(4);
      line(width/2, 100, width/2, 130);
      strokeWeight(1);
      fill(255);
      circle(width/2, 180, 100);
      noFill();
      line(width/2-56, 180, width/2-56, 180+l1);
      line(width/2+56, 180, width/2+56, 180+l2);
      arc(width/2, 180, 112, 112, PI, TWO_PI);
      fill(0);
      rect(width/2-56-m1*sizeOfBox, 180+l1, m1*sizeOfBox*2, m1*sizeOfBox*2);
      fill(255);
      text(str(m1), width/2-56-textWidth(str(m1))/2, 184+l1+m1*sizeOfBox);
      fill(0);
      rect(width/2+56-m2*sizeOfBox, 180+l2, m2*sizeOfBox*2, m2*sizeOfBox*2);
      fill(255);
      text(str(m2), width/2+56-textWidth(str(m2))/2, 184+l2+m2*sizeOfBox);
      break;
    case "Ground":
      if (l1 > 0 && l2 > 0) {
        a = ((-(m2*10))/(m1+m2))/(60*4);
        v+=a;
        println(v);
        a=0;
        l1 = l1 + v;
        l2 = l2 - v;
      }
      stroke(0);
      strokeWeight(4);
      strokeWeight(1);
      fill(255);
      circle(width-250+m1*sizeOfBox/2, 300-m1*sizeOfBox/2, m1*sizeOfBox);
      noFill();
      arc(width-250+m1*sizeOfBox/2, 300-m1*sizeOfBox/2, m1*sizeOfBox+4, m1*sizeOfBox+4, PI+HALF_PI, TWO_PI);
      fill(0);
      line(50, 300, width-250, 300);
      noFill();
      line(width-250+((m1*sizeOfBox)/2)-l1, 298-m1*sizeOfBox, width-250+m1*sizeOfBox/2, 298-m1*sizeOfBox);
      line(width-248+m2*sizeOfBox, 300-(m2*sizeOfBox/2), width-248+m2*sizeOfBox, 300+l2);
      fill(0);
      rect(width-250-l1-m1*sizeOfBox, 300-m1*sizeOfBox*2, m1*sizeOfBox*2, m1*sizeOfBox*2);
      fill(255);
      text(str(m1), width-250-l1+((m1*sizeOfBox)/2)-textWidth(str(m1)), 300-((m1*sizeOfBox)/2)-8);
      fill(0);
      rect(width-248, 300+l2, m2*sizeOfBox*2, m2*sizeOfBox*2);
      fill(255);
      text(str(m2), width-248+(m2*sizeOfBox)-textWidth(str(m2))/2, 300+l2+(m2*sizeOfBox/2)+16);
      break;
    case "Slope":
      println("Slope");
      break;
    case "both Slope":
      println("both Slope");
      break;
    }
  }
  lastTime = millis();
}
void mouseClicked() {
  if (b1.checkClick(mouseX, mouseY)) {
    status = "Float";
    v = 0;
    a = 0;
    l1 = 300;
    l2 = 300;
  } else if (b2.checkClick(mouseX, mouseY)) {
    status = "Ground";
    v = 0;
    a = 0;
    l1 = 300;
    l2 = 300;
  } else if (b3.checkClick(mouseX, mouseY)) {
    status = "Slope";
    v = 0;
    a = 0;
    l1 = 300;
    l2 = 300;
  } else if (b4.checkClick(mouseX, mouseY)) {
    status = "both Slope";
    v = 0;
    a = 0;
    l1 = 300;
    l2 = 300;
  }
}
