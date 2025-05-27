//record multiple key inputs

var map = {}; // You could also use an array
onkeydown = onkeyup = function (e) {
    e = e || event; // to deal with IE
    map[e.keyCode] = e.type == 'keydown';
    /* insert conditional here */
    if (map[17] && map[16] && map[65]) { // CTRL+SHIFT+A
        // CTRL+SHIFT+A
        if (currentPeriod) {
            tab2();
        }
        map = []
    } 
};

// ----------------------- //

//check if time is inbetween two vals
time = new Date();
var s = "12:30:12:40".split(":");
var dt1 = new Date(
    time.getFullYear(),
    time.getMonth(),
    time.getDate(),
    parseInt(s[0]),
    parseInt(s[1]),
    0
);

var e = "12:30:12:40".split(":");
var dt2 = new Date(
    time.getFullYear(),
    time.getMonth(),
    time.getDate(),
    parseInt(e[2]),
    parseInt(e[3]),
    0
);
if (time >= dt1 && time <= dt2) return true;
else return false
//returns a boolean which indicates if the time is in between the specified times

// ----------------------- //

//open new tabs function

function openInNewTab(url, codeForLaterRef) {
    if (url) {
        var win = window.open(url, codeForLaterRef);
    }
    return win;
}//returns a window object

// ----------------------- //

//notifications

function notifyMe(message) {
    if (message == undefined) {
        message = "Please provide a message";
    }
    if (!("Notification" in window)) {
        alert("This browser does not support desktop notification");
    } else if (Notification.permission === "granted") {
        var notification = new Notification(message);
    } else if (Notification.permission !== "denied") {
        Notification.requestPermission(function (permission) {
            if (permission === "granted") {
                var notification = new Notification("You will recieve messages here");
            }
        });
    }
}//doesnt return anything

// ----------------------- //