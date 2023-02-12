
PVector[] Circles = new PVector[4];
void setup() {
  size(500, 500);

  for (int i = 0; i < Circles.length-1; i++) {
    Circles[i] = new PVector(int(random(0, 500)), int(random(0, 500)));
  }
}
void draw() {
  Circles[Circles.length-1] = (new PVector(mouseX, mouseY));
  loadPixels();
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      int index = i + j*width;
      int mininum = 6000;
      int chosenBall = 0;
      for (int k = 0; k < Circles.length; k++) {
        int distance = int(dist(i, j, int(Circles[k].x), int(Circles[k].y)));
        if (mininum > distance) {
          mininum = distance;
          chosenBall = k;
        }
      }
      if (mininum!=0) {
        if (chosenBall==0){ 
          pixels[index] = color(pow((1/pow(mininum,2)), 2)*200000000, 0, 0);
        }else if (chosenBall==1){ 
          pixels[index] = color(0, pow((1/pow(mininum,2)), 2)*200000000, 0);
        }else if (chosenBall==2){ 
          pixels[index] = color(0, 0, pow((1/pow(mininum,2)), 2)*200000000);
        }else if (chosenBall==3){ 
          pixels[index] = color(pow((1/pow(mininum,2)), 2)*200000000, pow((1/pow(mininum,2)), 2)*200000000, pow((1/pow(mininum,2)), 2)*200000000);
        }
      }
    }
  }
  updatePixels();
  for (int i = 0; i < Circles.length; i++){
    Circles[i].x = ((Circles[i].x+random(-4, 4))%500);
  }
  for (int i = 0; i < Circles.length; i++){
    Circles[i].y = ((Circles[i].y+random(-4, 4))%500);
  }
}

class Circle{
  int x;
  int y;
  float acc;
  float vel;
  
}
