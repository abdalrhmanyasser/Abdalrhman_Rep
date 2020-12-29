var pdate;
var currentPeriod = "";
var currentday;
var date;
var s;
var win1;
var win3;
var win2;
var url1;
var url3;
var url2;
var previousPeriod = currentPeriod;
var dt1;
var boolea;
var thingy;
var sound;
var PeriodIndex = 1;
var listing = [
    ["Math",     "Math",     "English",  "break",    "Physics",  "H.S",     "Chemestry",    "break",    "break",    "break"],
    ["Physics",  "Math",     "Math",     "break",    "Physics",  "Arabic",  "H.S",          "break",    "break",    "break"],
    ["Physics",  "IS",       "English",  "break",    "Math",     "Arabic",  "H.s",          "break",    "break",    "break"],
    ["English",  "Chemestry","Physics",  "break",    "Arabic",   "So.St",   "Math",         "break",    "break",    "break"], 
    ["Chemestry","Math",     "So.St",    "break",    "Physics",  "CS",      "English",      "break",    "Arabic",   "Math" ]
];
var dict = {
    "1": "07:55:08:45",
    "2": "08:40:09:30",
    "3": "09:25:10:15",
    "4": "10:10:10:45",
    "5": "10:40:11:30",
    "6": "11:25:12:15",
    "7": "12:10:13:00",
    "8": "12:55:13:20",
    "9": "13:15:14:05",
    "10": "14:00:14:50"
};

function preload() {
    sound = new Audio(
        "https://cdn.glitch.com/348880f4-28cd-46f9-a35b-a5e6d6061d82%2FES_Beep%20Tone%20Signal%2054%20-%20SFX%20Producer.mp3?v=1606292991079"
    );
}

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
}

function openInNewTab(thing, currentperiod) {
    if (thing) {
        var win = window.open(thing, currentperiod);
    }
    return win;
}

function tab2() {
    switch (currentPeriod) {
        case "Science":
            var url1 = "contact abdalrhman with link for Science"; //google classroom
            var url2 = "contact abdalrhman with link for Science"; //google Meet
            var url3 = "contact abdalrhman with link for Science"; //periodic table
            tabs(url1, url2, url3);
            break;
    }
}

function setup() {
    noCanvas();
    win1 = open("/", "_blank");
    win2 = open("/", "_blank");
    win3 = open("/", "_blank");
    win1.close();
    win2.close();
    win3.close();

    pdate = new Date();
    setInterval(function () {
        currentday = pdate.getDay();
        var time = parseInt(
            pdate.getHours().toString() +
            (pdate.getMinutes().toString().length == 2 ?
                pdate.getMinutes().toString() :
                "0" + pdate.getMinutes().toString())
        );
        var time_box = document.getElementById("time");
        var hrs =
            pdate.getHours() > 12 ?
            (pdate.getHours() - 12).toString() :
            pdate.getHours().toString();
        var mins = pdate.getMinutes().toString();
        var secs = pdate.getSeconds().toString();
        if (hrs.length != 2) {
            hrs = "0" + hrs;
        }
        if (mins.length != 2) {
            mins = "0" + mins;
        }
        if (secs.length != 2) {
            secs = "0" + secs;
        }
        time_box.innerHTML =
            (hrs > 12 ? (hrs - 12).toString() : hrs.toString()) +
            ":" +
            pdate.getMinutes().toString() +
            ":" +
            secs;
        PeriodIndex = periodthigy(pdate);
        if (PeriodIndex >= 8 && currentday != 4) PeriodIndex = undefined;
        else if (PeriodIndex >= 8) PeriodIndex = int(PeriodIndex) - 1; 
        else if (PeriodIndex == 4) PeriodIndex = undefined;
        if (currentday != 5 && currentday != 6) {
                var current_period_html = document.getElementById(
                    (
                        "period" +
                        (currentday + 1) +
                        (PeriodIndex > 3 ? PeriodIndex - 1: PeriodIndex )
                    ).toString()
                );
            if (current_period_html != null) {
                current_period_html.style.backgroundColor = "#0000";
                time_box.innerHTML =
                    time_box.innerHTML + "<br>" + listing[currentday][PeriodIndex < 7 ? PeriodIndex - 1 : PeriodIndex];
            } else {
                time_box.innerHTML = time_box.innerHTML + "<br>" + "break";
            }

            currentPeriod = listing[currentday][PeriodIndex - 1];
            if (boolea == true) {
                sound.play();
                if (currentPeriod) {
                    tab2();
                    notifyMe("you have : " + currentPeriod);
                } else notifyMe("you have : break");
                boolea = false;
            }
            if (checkPeriod()) {
                boolea = true;
                previousPeriod = currentPeriod;
            }
            if (thingy == true) {
                currentPeriod = listing[currentday][PeriodIndex - 1];
                sound.play();
                if (currentPeriod) {
                    notifyMe("you have : " + currentPeriod + " in 10 mins");
                } else notifyMe("you have : break");
                thingy = false;
            }
            if (checkPeriod1()) {
                thingy = true;
            }
            var date = new Date();
        }
        pdate = new Date()
        pdate = new Date(
            pdate.getFullYear(),
            pdate.getMonth(),
            pdate.getDate(),
            pdate.getHours(),
            pdate.getMinutes(),
            pdate.getSeconds(),
            0
        );
    }, 1000);
}


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

function tabs(url1, url2, url3) {
    if (window.document.hasFocus()) {
        if (confirm('load new pages?')) {
            if (win1)
                if (!win1.closed)
                    win1.close();
            if (win2)
                if (!win2.closed)
                    win2.close();
            if (win3)
                if (!win3.closed)
                    win3.close();
            win1 = openInNewTab(url1, currentPeriod + "1");
            win3 = openInNewTab(url3, currentPeriod + "3");
            win2 = openInNewTab(url2, currentPeriod + "2");
            if (win2)
                win2.focus();
        }
    } else setTimeout(() => {
        sound.play()
        tabs(url1, url2, url3)
    }, 4000);
}

function periodthigy(time) {
    for (var key in dict) {
        var s = dict[key].split(":");
        var dt1 = new Date(
            time.getFullYear(),
            time.getMonth(),
            time.getDate(),
            parseInt(s[0]),
            parseInt(s[1]),
            0
        );

        var e = dict[key].split(":");
        var dt2 = new Date(
            time.getFullYear(),
            time.getMonth(),
            time.getDate(),
            parseInt(e[2]),
            parseInt(e[3]),
            0
        );
        if (time >= dt1 && time <= dt2) return key;
    }
}

function checkPeriod1() {
    for (var key in dict) {
            date = new Date();
            date = new Date(
                date.getFullYear(),
                date.getMonth(),
                date.getDate(),
                date.getHours(),
                date.getMinutes(),
                date.getSeconds(),
                0
            );
            s = dict[key].split(":");
            dt1 = new Date(
                date.getFullYear(),
                date.getMonth(),
                date.getDate(),
                parseInt(s[0]),
                parseInt(s[1]),
                0
            );

            if (date.getTime() == dt1.getTime()) {
                return true;
        }
    }
    return false;
}

function checkPeriod() {
    for (var key in dict) {
        date = new Date();
        date = new Date(
            date.getFullYear(),
            date.getMonth(),
            date.getDate(),
            date.getHours(),
            date.getMinutes(),
            date.getSeconds(),
            0
        );
        s = dict[key].split(":");
        var dt2 = new Date(
            date.getFullYear(),
            date.getMonth(),
            date.getDate(),
            parseInt(s[2]),
            parseInt(s[3]),
            0
        );

        if (date.getTime() == dt2.getTime() && previousPeriod != currentPeriod) {
            return true;
        }
    }
    return false;
}