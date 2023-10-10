import controlP5.*;
import javax.swing.JOptionPane;

boolean changedim = false;
String[] temp = new String[3];
boolean fullscreen;
String[][] PATHS;
PImage[] IMAGES;
int scale;
ControlP5 cp5;
String input1Value;
String input2Value;
MultiList l;
void controlEvent(ControlEvent theControlEvent) {
  if (theControlEvent.isTab()) {
    changedim = !changedim;
  }
}

void settings() {
  String[] dim = savedDim();
  if (isNumeric(dim[0]) && isNumeric(dim[1])) {
    size(int(dim[0]), int(dim[1]));
    fullscreen = false;
  } else {
      fullscreen = true;
      fullScreen();
  } 
}
void setup() {
  
  if (!fullscreen){surface.setLocation(100, 100);}
  ControlFont cfa = new ControlFont(createFont("Arial", int(height/19.0476190476)));
  ControlFont cf1 = new ControlFont(createFont("Arial", int(height/33.3333333333)));
  ControlFont cf2 = new ControlFont(createFont("Arial", int(height/44.4444444444)));
  ControlFont cf3 = new ControlFont(createFont("Arial", int(height/66.6666666667)));
  surface.setTitle("NOSER LAUNCHER");
  cp5 = new ControlP5(this);

  cp5.addTab("extra")
    .setColorBackground(color(0, 0, 0))
    .setColorLabel(color(255))
    .setColorActive(color(100, 100, 100))
    ;
  cp5.getTab("default")
    .setColorBackground(color(0, 0, 0))
    .setColorLabel(color(255))
    .setColorActive(color(40, 40, 40))
    .activateEvent(true)
    .setLabel("Games")
    .setId(1)
    .setHeight(30)
    .setWidth(70)
    ;
  cp5.getTab("extra")
    .setHeight(30)
    .setLabel("Change dimension")
    .activateEvent(true)
    .setId(2)
    .setWidth(100)
    ;
  Button size = cp5.addButton("dimChange")
    .setCaptionLabel("Change Window Size")
    .setPosition((width/2)-((width/6)/2)-(height/100), (height/2))
    .setSize((width/6)+(height/50), (height/12))
    .setColorLabel(color(0))
    .setColorBackground(color(255))
    .setColorActive(color(88, 88, 88))
    .setColorForeground(color(150, 150, 150))
    .setFont(cf2)
    ;
  Button b = cp5.addButton("ADDGAME")
    .setCaptionLabel("ADD GAME")
    .setPosition(0, height-(height/10))
    .setSize(width, (height/10))
    .setColorLabel(color(0))
    .setColorBackground(color(255))
    .setColorActive(color(88, 88, 88))
    .setColorForeground(color(150, 150, 150))
    .setFont(cfa)
    ;

  Textfield input1 = cp5.addTextfield("input1")
    .setPosition((width/2)-((width/6)/2)-(width/200), (height/2)-((height/8)/2)-(height/50))
    .setSize(width/12, height/16)
    .setFont(cf1)
    .setFocus(false)
    .setLabel("")
    .setAutoClear(false)
    .setColorBackground(color(255))
    .setColor(color(0))
    ;
  Textfield input2 = cp5.addTextfield("input2")
    .setPosition((width/2)+(width/200), (height/2)-((height/8)/2)-(height/50))
    .setSize(width/12, height/16)
    .setFont(cf1)
    .setAutoClear(false)
    .setFocus(false)
    .setLabel("")
    .setColorBackground(color(255))
    .setColor(color(0))
    ;
  Textlabel myTextlabelA = cp5.addLabel("scalelabel")
    .setText("Scale")
    .setPosition(180, 5)
    .setColorValue(color(0))
    .setFont(cf1)
    ;
  textSize(int(height/33.3333333333));
  Slider slider = cp5.addSlider("sc")
    .setPosition(200+textWidth("Scale"), 0)
    .setWidth(width/5)
    .setHeight(30)
    .setRange(3, 8)
    .showTickMarks(false)
    .setValue(5)
    .setNumberOfTickMarks(6)
    .setColorActive(color(100, 100, 100))
    .setColorForeground(color(100, 100, 100))
    ;
  // add a vertical slider
  cp5.addSlider("slider")
    .setPosition(width-30, 0)
    .setSize(30, height-height/10)
    .setRange(48, 0)
    .setValue(0)
    .setColorActive(color(0, 0, 0))
    .setColorForeground(color(0, 0, 0))
    .setHandleSize(10)
    .setScrollSensitivity(0.5)
    ;

  // reposition the Label for controller 'slider'
  cp5.getController("slider").getValueLabel().setVisible(false);
  cp5.getController("slider").getCaptionLabel().setVisible(false);
  cp5.getController("input1").moveTo("extra");
  cp5.getController("input2").moveTo("extra");
  cp5.getController("dimChange").moveTo("extra");
  cp5.getController("ADDGAME").moveTo("global");
  cp5.setAutoDraw(false);
  loadPaths();
  IMAGES = new PImage[PATHS.length];
  if (PATHS != null) {
    for (int i = 0; i < PATHS.length; i++) {
      IMAGES[i] = loadImage(PATHS[i][1]);
    }
  }

  int newWidth = width-30;
  scale = (newWidth)/5;
  for (int i = 0; i < IMAGES.length; i++) {
    IMAGES[i].resize(scale, int(scale*1.5));
  }
}
int n;
int m;
int i=0;
void mousePressed() {
  if (i==0) {
    m = millis();
  }
  if (mouseButton==LEFT) {
    i++;
    if (i==2) {
      n = millis();
    }
  }
}
void mouseReleased() {
  if (i==2 && n-m < 200)
  {
    int newWidth = width-30;
    float offset = ((((PATHS.length-1)*scale)/newWidth)*scale*2)*(cp5.getController("slider").getValue()/50);
    scale = (newWidth)/int(cp5.getController("sc").getValue());
    for (int i = 0; i < PATHS.length; i++) {
      int x = (((i*scale)+40)%newWidth)-40;
      float y =((i*scale+60)/newWidth)*scale*2-offset;
      if (mouseX>x && mouseX < x+scale && mouseY>y && mouseY<y+scale*2) {
        launch(PATHS[i][0]);
      }
    }
    i=0;
  } else if (i>1) {
    i=0;
  }
}
void mouseWheel(MouseEvent event) {
  float e = event.getCount();
  if (mouseY>30 && mouseY<height-(height/10)) {
    cp5.getController("slider").setValue(cp5.getController("slider").getValue()+e);
  }
}
public static boolean isNumeric(String str) {
  try {
    double d = Double.parseDouble(str);
  }
  catch (NumberFormatException e) {
    return false;
  }
  return true;
}
void sc() {
  int newWidth = width-30;
  try {
    scale = (newWidth)/int(cp5.getController("sc").getValue());
    for (int i = 0; i < IMAGES.length; i++) {
      IMAGES[i].resize(scale, int(scale*1.5));
    }
  }
  catch(Exception e) {
    println(e);
  }
}
void keyPressed() {
  if (key == CODED) {
    println(keyCode);
    if (keyCode == 122) {
      if (fullscreen) {
        writeToFile("1200 800", "dim.nl");
        exit();
      } else {
        writeToFile("fullscreen", "dim.nl");
        exit();
      }
    }
  }
}
void draw() {
  int newWidth = width-30;
  scale = (newWidth)/int(cp5.getController("sc").getValue());
  background(255, 255, 255);

  input1Value = cp5.get(Textfield.class, "input1").getText();
  input2Value = cp5.get(Textfield.class, "input2").getText();
  fill(0, 0, 0, 0);
  stroke(0);
  strokeWeight(2);
  float offset;
  try {
    offset = ((((PATHS.length-1)*scale)/newWidth)*scale*2)*(cp5.getController("slider").getValue()/50);
  }
  catch(Exception e) {
    offset = 0;
  }
  if (PATHS != null) {
    for (int i = 0; i < PATHS.length; i++) {
      fill(0, 0, 0, 0);
      stroke(0, 0, 0);
      strokeWeight(1);
      int x = (((i*scale)+40)%newWidth)-40;
      float y =((i*scale+60)/newWidth)*scale*2-offset;
      rect(x, y, scale, scale*2,7);
      try {
        image(IMAGES[i], x, y);
      }
      catch(Exception e) {
        println(e);
      }
      stroke(0);
      fill(0);
      strokeWeight(5);
      textSize(((height/19))-cp5.getController("sc").getValue()-((height/44.4444444444))); 
      if (PATHS[i] != null) {
        if (PATHS[i][2] != null) {
          text(PATHS[i][2], x+20, y+(scale*1.75));
        }
      }
    }
  }
  strokeWeight(0);
  fill(255);
  rect(0, 0, width, 30);
  cp5.draw();
  fill(0, 0, 0, 0);
  rect(0, height-(height/10), width-2, (height/10)-2, 10);

  if (changedim) {
    stroke(30, 30, 30);
    fill(30, 30, 30, 30);
    rect(0, 0, width, height);
    stroke(255);
    fill(255);
    rect(width/2-width/10, height/2-height/10, width/5, height/5);
    cp5.draw();
  }
  stroke(100);
  fill(100, 100, 100);
  strokeWeight(2);
  rect(width-30, ((cp5.getController("slider").getValue()/48)*(height-(height/10)-30)), 30, 30);
  textSize(14);
  text("MADE BY ABDALRHMAN YASER", width-textWidth("MADE BY ABDALRHMAN YASER  "), height-2);
}

void dimChange() {
  if (int(input1Value) >400 && int(input2Value)>500){
    writeToFile(input1Value+" "+input2Value, "dim.nl");
    exit();
  }
}
String[] savedDim() {
  try {
    String[] lines = loadStrings("dim.nl");
    return lines[0].split(" ");
  }
  catch (Exception e) {
    println(e.toString());
    writeToFile("1200 800", "dim.nl");
    String[] lines = {"1200", "800"};
    return lines;
  }
}
void loadPaths() {
  String[] lines = {""};
  try {
    lines = loadStrings("data.nl");
    if (lines == null) {
      println("file does not exist making a new one");
      PrintWriter writer;
      writer = createWriter("data.nl");
      writer.flush(); // Flush the buffer to ensure data is written
      writer.close(); // Close the file
      loadPaths();
      return;
    }
  }
  catch (Exception e) {
    println(e);
  }
  PATHS = new String[lines.length][3];  // Initialize the PATHS array with proper dimensions
  for (int i = 0; i < lines.length; i++) {
    String[] splitLines = lines[i].split("@%20%@");
    for (int j = 0; j<splitLines.length; j++) {
      PATHS[i][j] = splitLines[j];
    }
  }
}
public void ADDGAME() {
  selectInput("Select a the exe of the Game:", "GAMEPATHSELECTED");
}
public void GAMEPATHSELECTED(File fileselected) {
  if (fileselected == null) {
    println("No file selected.");
    temp = new String[3];
    return;
  }
  temp[0] = fileselected.getAbsolutePath();
  selectInput("Select the pic of the Game:", "GAMEPICSELECTED");
}
public void GAMEPICSELECTED(File fileselected) {
  if (fileselected == null) {
    println("No file selected.");
    temp = new String[3];
    return;
  }
  temp[1] = fileselected.getAbsolutePath();
  String userInput = JOptionPane.showInputDialog("Enter the Name of the Game:");
  temp[2] = userInput;
  String allpathstr = "";
  for (int i = 0; i < PATHS.length; i++) {
    for (int j = 0; j < PATHS[i].length; j++) {
      allpathstr+=PATHS[i][j];
      if (j != PATHS[i].length-1) {
        allpathstr+="@%20%@";
      }
    }
    if (i < PATHS.length-1) {
      allpathstr+="\n";
    }
  }
  if (PATHS.length != 0) {
    if (PATHS[0][0] != "") {
      allpathstr+="\n";
    }
  }
  allpathstr+=temp[0]+"@%20%@"+temp[1]+"@%20%@"+temp[2];
  writeToFile(allpathstr, "data.nl");
  loadPaths();
}
void writeToFile(String content, String Path) {
  PrintWriter writer = createWriter(Path); // Create or overwrite the file
  writer.println(content); // Write a line of content to the file
  writer.flush(); // Flush the buffer to ensure data is written
  writer.close(); // Close the file
}
