PFont f;
int scale = 10;
boolean gridsnap = false;
boolean aInitilised = false;
boolean bInitilised = false;
float x = 10;
float y = 10;
float w = 40;
float h = 30;
class Point {
  public float x;
  public float y;
  public float xFull;
  public float yFull;
  public Point(float _x, float _y) {
    x = _x / (float)width * scale;
    y = _y / (float)height * scale;
    xFull = _x;
    yFull = _y;
  }
  public Point(float _x, float _y, boolean isFull) {
    if (isFull) {
      if (gridsnap) {
        x = (float)round(_x / (float)width * scale);
        y = (float)round(_y / (float)height * scale);
        xFull = (float)round(x * (float)width / scale);
        yFull = (float)round(y * (float)height / scale);
      } else {
        x = _x / (float)width * scale;
        y = _y / (float)height * scale;
        xFull = _x;
        yFull = _y;
      }
    } else {
      x = _x;
      y = _y;
      xFull = _x * width / scale;
      yFull = _y * height / scale;
    }
  }
}
Point  a;
Point  b;
Point  aFake;
Point  bFake;
void setup() {
  size(600, 600);
  f = createFont("Arial", 16, true);
}

void mouseReleased() {
  if (mouseY < height - 100) {
    if (!aInitilised) {
      a = new Point(mouseX, mouseY, true);
      aInitilised = true;
    } else if (!bInitilised) {
      b = new Point(mouseX, mouseY, true);
      float s =  (a.y - b.y) / (a.x - b.x);
      if (a.x - b.x != 0 && a.y - b.y != 0 && s > 0.1) {
        aFake = new Point(a.xFull + 1000, a.yFull + (abs(s) * 1000), true);
        bFake = new Point(b.xFull - 1000, b.yFull - (abs(s) * 1000), true);
      } else if (a.x - b.x != 0 && a.y - b.y != 0 && s < -0.1) {
        aFake = new Point(a.xFull + 1000, a.yFull - (abs(s) * 1000), true);
        bFake = new Point(b.xFull - 1000, b.yFull + (abs(s) * 1000), true);
      } else if (a.x - b.x == 0) {
        aFake = new Point(a.xFull, a.yFull - 500, true);
        bFake = new Point(b.xFull, b.yFull + 500, true);
      } else if (a.y - b.y == 0) {
        aFake = new Point(a.xFull- 500, a.yFull, true);
        bFake = new Point(b.xFull + 500, b.yFull, true);
      }
      bInitilised = true;
    }
  }
}

void draw() {
  if (mouseY < height - 100) {
    Point temp = new Point(mouseX, mouseY, true);
    background(255);
    strokeWeight(1);
    stroke(0, 100);
    for (int i = 0; i<scale; i++) {
      line(width / scale * i, 0, width / scale * i, height- 100);
    }
    for (int i = 0; i<scale- 1; i++) {
      line(0, height / scale * i, width, height / scale * i);
    }
    fill(255);
    rect(0, height - 100, width, height);
    textSize(16+8);
    textAlign(LEFT);
    textSize(8);
    for (int i = 0; i < scale; i++) {
      for (int j = 0; j < scale - 1; j++) {
        text(String.format("%d, %d", i, j), i * width / scale, j *height /  scale);
      }
    }
    strokeWeight(10);
    stroke(0);
    point(temp.xFull, temp.yFull);
    textSize(8);
    textFont(f);
    fill(255, 0, 0);
    textAlign(LEFT);

    if (!aInitilised) {
    } else if (!bInitilised) {
      point(a.xFull, a.yFull);
      text(String.format("a(%.2f, %.2f)", a.x, a.y), a.xFull + 10, a.yFull - 10);
    } else {
      fill(0);
      textAlign(LEFT);
      textSize(20);
      text(String.format("%.2f - %.2f\n――――― = %.2f\n%.2f - %.2f", a.y, b.y, ((b.y - a.y) / (b.x - a.x)), a.x, b.x), width - 200, height - 75);
      text("Slope is", width - 300, height - 50);
      textSize(24);
      textAlign(LEFT);
      text("Press 'r' to reset the Points\nPress 'f' to Enable Grid snapping", 10, height - 50);
      Point c = new Point(mouseX, mouseY, true);

      stroke(0);
      strokeWeight(3);
      line(aFake.xFull, aFake.yFull, bFake.xFull, bFake.yFull);
      strokeWeight(10);

      textFont(f);
      fill(255, 0, 0);
      textAlign(TOP, LEFT);

      point(a.xFull, a.yFull);
      text(String.format("a(%.2f, %.2f)", a.x, a.y), a.xFull + 10, a.yFull - 10);

      point(b.xFull, b.yFull);
      text(String.format("b(%.2f, %.2f)", b.x, b.y), b.xFull - 40, b.yFull - 10);

      Point p = scalarProjection(c, a, b);
      stroke(255, 0, 0);
      strokeWeight(3);
      line(p.xFull, p.yFull, c.xFull, c.yFull);
      Point midPoint = new Point((p.x + c.x) / 2, (p.y + c.y) / 2, false);
      text(String.format("%.2f", (dist(p.x, p.y, c.x, c.y))), midPoint.xFull + 10, midPoint.yFull + 10);
      point(c.xFull, c.yFull);
      text(String.format("c(%.2f, %.2f)", c.x, c.y), c.xFull + 10, c.yFull - 10);
      strokeWeight(10);
      stroke(0);
      point(p.xFull, p.yFull);
      text(String.format("a: (%.2f, %.2f)\nb: (%.2f, %.2f)\nc: (%.2f, %.2f)\ndistance:%.2f", a.x, a.y, b.x, b.y, c.x, c.y, dist(p.x, p.y, c.x, c.y)), 10, 30);
    }
  }
}
Point scalarProjection(Point p, Point a, Point b) {
  PVector avec = new PVector(a.xFull, a.yFull);
  PVector bvec = new PVector(b.xFull, b.yFull);
  PVector pvec = new PVector(p.xFull, p.yFull);
  PVector ap = PVector.sub(pvec, avec);
  PVector ab = PVector.sub(bvec, avec);
  ab.normalize(); // Normalize the line
  ab.mult(ap.dot(ab));
  PVector normalPoint = PVector.add(avec, ab);
  return new Point(normalPoint.x, normalPoint.y);
}
void keyPressed() {
  if ( key == 'f') {
    gridsnap = gridsnap ? false : true;
  }
  if ( key == 'r') {
    reset();
  }
}

void reset() {
  aInitilised = false;
  bInitilised = false;
}
