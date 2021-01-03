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
    ['Math', 'Science', 'Electives', 'Arabic', 'Islamic', 'English', 'PE'], 
    ['Arabic', 'Electives', 'Science', 'Islamic', 'English', 'Math', 'PE'],
    ['English', 'Islamic', 'Math', 'Electives', 'Moral_Education', 'Arabic', 'Science'], 
    ['PE', 'Arabic', 'Electives', 'Math', 'Science', 'English', 'Math'], 
    ['English', 'Science', 'Math', 'Electives', 'PE', 'English', 'Arabic']
    ];
var dict = {
    "1": "07:55:08:40",
    "2": "08:35:09:25",
    "3": "09:20:10:10",
    "4": "10:05:10:55",
    "5": "11:00:11:40",
    "6": "11:35:12:25",
    "7": "12:20:13:10",
    "8": "13:05:13:55"
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
            var url1 = "https://classroom.google.com/u/1/c/MTUyOTgyNzUyOTAz"; //google classroom
            var url2 = "https://meet.google.com/lookup/gekwp53xjl?authuser=1&hs=179"; //google Meet
            var url3 = "https://ptable.com/?lang=en#Properties"; //periodic table
            tabs(url1, url2, url3);
            break;
        case "Electives":
            var url1 = "https://classroom.google.com/u/1/c/MTUzMDI1MDY0Nzgy"; //google classroom
            var url2 = "https://meet.google.com/lookup/egffjbewtc?authuser=1&hs=179"; //google Meet
            var url3 = ""; //periodic table
            tabs(url1, url2, url3);
            break;
        case "Arabic":
            var url1 = "https://classroom.google.com/u/1/c/MTUyNzA1NzgzNDUw"; //google classroom
            var url2 = "https://meet.google.com/lookup/bvm6h4ht4j?authuser=1&hs=179"; //google Meet
            var url3 = "https://sso.alefed.com/"; //alef education
            tabs(url1, url2, url3);
            break;
        case "English":
            var url1 = "https://classroom.google.com/u/1/c/MTU5MjU2MjM3NDAz"; //google classroom
            var url2 = "https://meet.google.com/lookup/ct4xgqea53?authuser=1&hs=179"; //google Meet
            var url3 = "";
            tabs(url1, url2, url3);
            break;
        case "Math":
            var url1 = "https://classroom.google.com/u/1/w/MTUyODYyNTUzNDI2/t/all"; //google classroom
            var url2 = "https://meet.google.com/lookup/bwzrmrjprl?authuser=1&hs=179"; //google Meet
            var url3 = "";
            tabs(url1, url2, url3);
            break;
        case "Islamic":
            var url1 = "https://classroom.google.com/u/1/c/MTUyOTAwMjgyMzU5"; //google classroom
            var url2 = "https://meet.google.com/lookup/g6hjyuedmt?authuser=1&hs=179"; //google Meet
            var url3 = "https://equran.me/browse.html"; //quran
            tabs(url1, url2, url3);
            break;
        case "PE":
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
        PeriodIndex = periodthigy(pdate) - 1;
        if (currentday != 5 && currentday != 6) {
            var current_period_html = document.getElementById(
                (
                    "period" +
                    (currentday + 1) +
                    (PeriodIndex > 3 ? PeriodIndex : PeriodIndex + 1)
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
                sound.play();
                if (currentPeriod) {
                    tab2();
                    notifyMe("you have : " + currentPeriod);
                } else notifyMe("you have : break");
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
            var date = new Date();
        }
        pdate = new Date();

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
            win1 = openInNewTab(url1, currentPeriod + "1");
            win3 = openInNewTab(url3, currentPeriod + "3");
            win2 = openInNewTab(url2, currentPeriod + "2");
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
        if (time >= dt1 && time <= dt2) return key;
    }
}

function checkPeriod1() {
    for (var key in dict) {
        if (key != 4) {
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

        if (date.getTime() == dt2.getTime()) {
            return true;
        }
    }
    return false;
}