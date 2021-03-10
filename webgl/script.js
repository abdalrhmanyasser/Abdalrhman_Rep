const ROW = 50;
const COL = 50;
const WIDTH = 1000;
const HEIGHT = 1000;
const CELL_HEIGHT = HEIGHT/ROW;
const CELL_WIDTH = WIDTH/COL;
var cells = [];
var nabrs = [];
var start = false;
var textbox;
var Interval_ID;

class Cell{
    constructor(x,y,state){
        this.x = x; // row
        this.y = y; // col
        this.state = state;
        this.nabrs = 0;
    }

    print() {
        strokeWeight(4)
        if (this.state == "dead"){
            fill(155);
        }else if (this.state == "alive"){
            fill(255);
        }
        rect((this.y)*CELL_WIDTH, (this.x)*CELL_HEIGHT, (this.y+1)*CELL_WIDTH, (this.x+1)*CELL_HEIGHT);
    }
    increamentNabrs(){this.nabrs++}
}

function checkNabour(cells,cell){
    for (let y = 0; y < 3;y++){
        for (let x = 0; x < 3;x++){
            if(!(cell.y == 0    && y == 0)
            && !(cell.y == ROW-1&& y == 2)
            && !(cell.x == 0    && x == 0)
            && !(cell.x == COL-1&& x == 2)
            )
            {
                if (!(x==1 && y==1))
                if (cells[cell.y + y - 1][cell.x + x - 1].state == "alive"){cell.increamentNabrs()}
            }
        }
    }
}

function mouseClicked(){
    var mousex = floor((mouseX < WIDTH ? mouseX : undefined)/CELL_WIDTH)
    var mousey = floor((mouseY < HEIGHT ? mouseY : undefined)/CELL_HEIGHT)
    if (!isNaN(mousex) && !isNaN(mousey)){
        console.log(mousex, mousey)
        newCELL(mousex, mousey)
    }
} 
function newCELL(x, y){
    if(cells[y][x].state == 'alive')cells[y][x].state = 'dead'
    else cells[y][x].state = 'alive'
}

function createCells() {
    for (let x  = 0; x  < ROW; x++) {
        var r = []
        for (let y = 0; y < COL; y++) {
            r.push(new Cell(x, y, "dead"))
        }
        cells.push(r)
        
    }
}
function startSim(){
    start = !start
    if(start){
        clearInterval(Interval_ID);
        setInter(textbox.value())
    }
}
function setup() {
    createCanvas(WIDTH,HEIGHT);
    createCells();            
    btn = createButton("Start")
    btn.mousePressed(startSim)
    textbox = createInput("1000")
}
function setInter(speed){
    Interval_ID = setInterval(()=>{
        if(start){
            nabrs = []
            for (let y  = 0; y  < ROW; y++) {
                var r = []
                for (let x = 0; x < COL; x++) {
                    cells[x][y].nabrs = 0
                    checkNabour(cells, cells[x][y])
                    r.push(cells[x][y].nabrs)
                }
                nabrs.push(r)
            }
            var newarr = cells
            for (var y = 0; y < ROW;y++){
                for (var x = 0; x < COL;x++){
                    if (nabrs[y][x] > 3 && newarr[y][x].state == 'alive')
                    {
                        cells[y][x].state = 'dead'
                    }
                    else if (nabrs[y][x] < 2 && newarr[y][x].state == 'alive')
                    {
                        cells[y][x].state = 'dead'
                    }
                    else if (nabrs[y][x] == 3)
                    {
                        cells[y][x].state = 'alive'
                    }
                }
            }
        }
    }, parseInt(speed))
    console.log(parseInt(speed));
    console.log(speed)
}
function draw(){
    background(75);
    for (let y  = 0; y  < ROW; y++) {
        for (let x = 0; x < COL; x++) {
            cells[x][y].print()
        }
    }
}