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
var dt1;
var boolea;
var thingy;
var sound;
var PeriodIndex = 0;
var listing = [
    ['English', 'Math', 'ESS', 'Electives', 'Science', 'Arabic', 'Islamic'], 
    ['Math', 'ESS', 'Math', 'Electives', 'English', 'Science', 'Arabic'], 
    ['English', 'Arabic', 'Science', 'Electives', 'Math', 'ESS', 'Moral_Education'], 
    ['English', 'Science', 'Math', 'Electives', 'Islamic', 'ESS', 'Arabic'], 
    ['English', 'ESS', 'Science', 'Arabic', 'Math', 'English', 'Islamic']
    ];
var dict = {
    "1": "08:00:08:40",
    "2": "08:45:09:25",
    "3": "09:30:10:10",
    "4": "10:15:10:55",
    "5": "11:00:11:40",
    "6": "11:45:12:25",
    "7": "12:25:12:30",
    "8": "12:35:13:10",
    "9": "13:15:13:55"
};

function preload() {
    sound = new Audio(
        "ES_Beep%20Tone%20Signal%2054%20-%20SFX%20Producer.mp3"
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
function tab2(_currentPeriod) {
    switch ((_currentPeriod).toLowerCase()) {
        case "science":
            var url1 = "https://classroom.google.com/u/1/c/MTUyOTgyNzUyOTAz"; //google classroom
            var url2 = "https://meet.google.com/lookup/gekwp53xjl?authuser=1&hs=179"; //google Meet
            var url3 = "https://ptable.com/?lang=en#Properties"; //periodic table
            tabs(url1, url2, url3);
            break;
        case "electives":
            var url1 = "https://classroom.google.com/u/1/c/MjQ2MjEwNjgwNzkw"; //google classroom
            var url2 = "https://meet.google.com/lookup/doqoq3pvcu?authuser=1&hs=179"; //google Meet
            var url3 = ""; //periodic table
            tabs(url1, url2, url3);
            break;
        case "arabic":
            var url1 = "https://classroom.google.com/u/1/c/MTUyNzA1NzgzNDUw"; //google classroom
            var url2 = "https://meet.google.com/lookup/bvm6h4ht4j?authuser=1&hs=179"; //google Meet
            var url3 = "https://sso.alefed.com/"; //alef education
            tabs(url1, url2, url3);
            break;
        case "english":
            var url1 = "https://classroom.google.com/u/1/c/MTU5MjU2MjM3NDAz"; //google classroom
            var url2 = "https://readtheory.org/app/student/quiz";
            var url3 = "https://meet.google.com/lookup/ct4xgqea53?authuser=1&hs=179"; //google Meet
            tabs(url1, url2, url3);
            break;
        case "math":
            var url1 = "https://classroom.google.com/u/1/w/MTUyODYyNTUzNDI2/t/all"; //google classroom
            var url2 = "https://meet.google.com/lookup/bwzrmrjprl?authuser=1&hs=179"; //google Meet
            var url3 = "";
            tabs(url1, url2, url3);
            break;
        case "islamic":
            var url1 = "https://classroom.google.com/u/1/c/MTUyOTAwMjgyMzU5"; //google classroom
            var url2 = "https://meet.google.com/lookup/g6hjyuedmt?authuser=1&hs=179"; //google Meet
            var url3 = "https://equran.me/browse.html"; //quran
            tabs(url1, url2, url3);
            break;
        case "ess":
            var url1 = "https://classroom.google.com/u/1/c/MjQ2MjE0NzY4NzMx"; //N/a
            var url2 = "https://meet.google.com/lookup/d2nnvbhmtn?authuser=1&hs=179"; //N/a
            var url3 = ""; //N/a
            tabs(url1, url2, url3);
            break;
        case "n/a":
            var url1 = ""; //N/a
            var url2 = ""; //N/a
            var url3 = ""; //N/a
            tabs(url1, url2, url3);
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
        if (currentday != 5 && currentday != 6) {
            
            PeriodIndex -= 1;
            
            var current_period_html = document.getElementById(
                (
                    "period" +
                    (currentday + 1) +
                    (PeriodIndex + 1)
                ).toString()
            );
            if (current_period_html != null) {
                current_period_html.style.backgroundColor = "#0000";
                time_box.innerHTML =
                    time_box.innerHTML + "<br>" + listing[currentday][PeriodIndex];
            } else {
                time_box.innerHTML = time_box.innerHTML + "<br>" + "break";
            }

            currentPeriod = listing[currentday][PeriodIndex];
            if (boolea == true) {
                if (currentPeriod) {
                    sound.play();
                    notifyMe("you have : " + currentPeriod);
                    tab2(currentPeriod);
                }else{
                    var dt1 = new Date(
                        pdate.getFullYear(),
                        pdate.getMonth(),
                        pdate.getDate(),
                        14,
                        0,
                        1,
                        0
                    );
                    if (dt1.getTime() == pdate.getTime()) {
                        tab2("n/a")
                    };
                }
                boolea = false;
            }
            if (checkPeriod()) {
                boolea = true;
            }
            if (thingy == true) {
                currentPeriod = listing[currentday][PeriodIndex + 1];
                sound.play();
                if (currentPeriod) {
                    notifyMe("you have : " + currentPeriod + " in 10 mins");
                } else notifyMe("you have : break");
                thingy = false;
            }
            if (checkPeriod1()) {
                thingy = true;
            }
        }
        date= new Date();
        pdate = new Date(
            date.getFullYear(),
            date.getMonth(),
            date.getDate(),
            date.getHours(), 
            date.getMinutes(),
            date.getSeconds(), 
            0);
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
            tab2(currentPeriod);
        }
        map = []
    }
};

function tabs(url1, url2, url3) {
    if (window.document.hasFocus()){
        if (confirm('load new pages?')){
            if (win1)
                if (!win1.closed)
                    win1.close();
            if (win2)
                if (!win2.closed)
                    win2.close();
            if (win3)
                if (!win3.closed)
                    win3.close();
            win1 = openInNewTab(url1, "1");
            win3 = openInNewTab(url3, "3");
            win2 = openInNewTab(url2, "2");
            if (win2)
                win2.focus();
        }
    }else setTimeout(() => {
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
        if (time >= dt1 && time <= dt2 && key < 5) return key;
        else if (time >= dt1 && time <= dt2 && key == 6) return key - 1;
        else if (time >= dt1 && time <= dt2 && key > 7) return key - 2;
    }
}

function checkPeriod1() {
    for (var key in dict) {
        if (key != 5 || key != 7) {
            date = new Date(
                pdate.getFullYear(),
                pdate.getMonth(),
                pdate.getDate(),
                pdate.getHours(),
                pdate.getMinutes(),
                pdate.getSeconds(),
                0
            );
            s = dict[key].split(":");
            dt1 = new Date(
                pdate.getFullYear(),
                pdate.getMonth(),
                pdate.getDate(),
                parseInt(s[0]),
                parseInt(s[1])- 10,
                0,
                0
            );
            if (date.getTime() == dt1.getTime()) {
                return true;
            }
        }
    }
    return false;
}

function checkPeriod() {
    for (var key in dict) {
        date = new Date(
            pdate.getFullYear(),
            pdate.getMonth(),
            pdate.getDate(),
            pdate.getHours(),
            pdate.getMinutes(),
            pdate.getSeconds(),
            0
        );
        s = dict[key].split(":");
        var dt2 = new Date(
            pdate.getFullYear(),
            pdate.getMonth(),
            pdate.getDate(),
            parseInt(s[2]),
            parseInt(s[3]) + 5,
            0,
            0
        );
        if (date.getTime() == dt2.getTime()) {
            return true;
        }
    }
    return false;
}