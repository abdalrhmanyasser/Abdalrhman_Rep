var sound;
var i = 50;
/**
 * opening sidebar / closing it
 */
function toggleSidebar() {
    if (mini) {
        document.getElementById("mySidebar").style.width = "340px";
        document.getElementById("main").style.marginLeft = "340px";
        this.mini = false;
    } else {
        document.getElementById("mySidebar").style.width = "65px";
        document.getElementById("main").style.marginLeft = "65px";
        this.mini = true;
    }
}


/**
 * notification method, may want to improve this function later
 * @param {String} message to be displayed
 * @returns nothing
 */
function notifyMe(message) {
    if (message == undefined) {
        message = "Please provide a message";
        return
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
/**
 * function open the link with the naming of current period
 * @param {String} link link to open
 * @param {String} currentperiod backend name of the web page
 * @returns the win just opened
 */
function openInNewTab(link, currentperiod) {
    if (link) {
        var win = window.open(link, currentperiod);
    }
    return win;
}

/**
 * function to open the links needed for the current period given from param _currentPeriod
 * @param {String} _currentPeriod 
 */
function tab2(_currentPeriod) {
    switch ((_currentPeriod).toLowerCase()) {
        case "science":
            var url1 = "https://classroom.google.com/u/" + authuser + "/c/MTUyOTgyNzUyOTAz"; //google classroom
            var url2 = "https://meet.google.com/lookup/gekwp53xjl?authuser=" + authuser + "&hs=179"; //google Meet
            var url3 = "https://ptable.com/?lang=en#Properties"; //periodic table
            tabs(url1, url2, url3);
            break;
        case "electives":
            var url1 = "https://classroom.google.com/u/" + authuser + "/c/MjQ2MjEwNjgwNzkw"; //google classroom
            var url2 = "https://meet.google.com/lookup/doqoq3pvcu?authuser=" + authuser + "&hs=179"; //google Meet
            var url3 = ""; //periodic table
            tabs(url1, url2, url3);
            break;
        case "arabic":
            var url1 = "https://classroom.google.com/u/" + authuser + "/c/MTUyNzA1NzgzNDUw"; //google classroom
            var url2 = "https://meet.google.com/lookup/bvm6h4ht4j?authuser=" + authuser + "&hs=179"; //google Meet
            var url3 = "https://sso.alefed.com/"; //alef education
            tabs(url1, url2, url3);
            break;
        case "english":
            var url1 = "https://classroom.google.com/u/" + authuser + "/c/MTU5MjU2MjM3NDAz"; //google classroom
            var url2 = "https://meet.google.com/lookup/ct4xgqea53?authuser=" + authuser + "&hs=179"; //google Meet
            var url3 = "https://readtheory.org/app/student/quiz";
            tabs(url1, url2, url3);
            break;
        case "math":
            var url1 = "https://classroom.google.com/u/" + authuser + "/w/MTUyODYyNTUzNDI2/t/all"; //google classroom
            var url2 = "https://meet.google.com/lookup/bwzrmrjprl?authuser=" + authuser + "&hs=179"; //google Meet
            var url3 = "";
            tabs(url1, url2, url3);
            break;
        case "islamic":
            var url1 = "https://classroom.google.com/u/" + authuser + "/c/MTUyOTAwMjgyMzU5"; //google classroom
            var url2 = "https://meet.google.com/lookup/g6hjyuedmt?authuser=" + authuser + "&hs=179"; //google Meet
            var url3 = "https://equran.me/browse.html"; //quran
            tabs(url1, url2, url3);
            break;
        case "ess":
            var url1 = "https://classroom.google.com/u/" + authuser + "/c/MjQ2MjE0NzY4NzMx"; //N/a
            var url2 = "https://meet.google.com/lookup/d2nnvbhmtn?authuser=" + authuser + "&hs=179"; //N/a
            var url3 = "https://www.savvasrealize.com/community/program"; //N/a
            tabs(url1, url2, url3);
            break;
        case "n/a":
            var url1 = ""; //N/a
            var url2 = ""; //N/a
            var url3 = ""; //N/a
            tabs(url1, url2, url3);
    }
}

function mousePressed() {
    userStartAudio();
}

// function happens when all functions are made and done
function setup() {
    // mimics the autoplay policy
    getAudioContext().suspend();

    //this is for the sound effects
    sound = document.getElementById("audio");

    // no canvas because p5js is a main library
    noCanvas();
    //initilizing win vars 
    win1 = open("/", "_blank");
    win2 = open("/", "_blank");
    win3 = open("/", "_blank");
    win1.close();
    win2.close();
    win3.close();

    // this is for updating the timetable and other content aka main loop
    refoundDate = new Date();
    setInterval(function () {
        // this is for finding the day, time and formating them to be compatible with our constants
        currentday = refoundDate.getDay();
        var time_box = document.getElementById("time");
        var hrs =
            refoundDate.getHours() > 12 ?
            (refoundDate.getHours() - 12).toString() :
            refoundDate.getHours().toString();
        var mins = refoundDate.getMinutes().toString();
        var secs = refoundDate.getSeconds().toString();
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
            mins +
            ":" +
            secs;
        PeriodIndex = Check_Period_Now(refoundDate);
        // checking if the day is 5 friday or 6 saterday, because there is no need to update on the weekend
        if (currentday != 5 && currentday != 6) {
            PeriodIndex -= 1;
            var fakePeriodIndex = PeriodIndex;
            // find document element to highlight
            console.log(PeriodIndex, listing[currentday][PeriodIndex])
            if (listing[currentday][PeriodIndex] != 'break' && listing[currentday][PeriodIndex] != undefined) {
                if (listing[currentday][PeriodIndex - 1] == 'break'){
                    fakePeriodIndex--;
                }
                if (listing[currentday][PeriodIndex - 2] == 'break'){
                    fakePeriodIndex--;
                }
                if (listing[currentday][PeriodIndex - 3] == 'break'){
                    fakePeriodIndex--;
                }
                if (listing[currentday][PeriodIndex - 4] == 'break'){
                    fakePeriodIndex--;
                }
                console.log("we went in!!!!!", fakePeriodIndex, listing[currentday][PeriodIndex])

                var current_period_html = document.getElementById(
                    (
                        "period" +
                        (currentday + 1) +
                        (fakePeriodIndex + 1)
                    ).toString()
                );
                // coloring the above found element
                if (current_period_html != null) {
                    current_period_html.style.backgroundColor = "#0000";
                    time_box.innerHTML =
                        time_box.innerHTML + "<br>" + listing[currentday][PeriodIndex];
                }
            } else {
                time_box.innerHTML = time_box.innerHTML + "<br>" + "break";
            }
            //finding the current period
            currentPeriod = listing[currentday][PeriodIndex];
            // checking boolean A because we dont want to do the update and the link sending before we finish another tick
            if (boolean_a == true) {
                if (currentPeriod) {
                    notifyMe("you have : " + currentPeriod);
                    sound.play();
                    setTimeout(tab2, 1100, (currentPeriod));
                } else {
                    //checking if it the end of the day
                    var dt1 = new Date(
                        refoundDate.getFullYear(),
                        refoundDate.getMonth(),
                        refoundDate.getDate(),
                        13,
                        30,
                        1,
                        0
                    );
                    if (dt1.getTime() == refoundDate.getTime()) {
                        tab2("n/a")
                    };
                }
                if (listing[currentday][PeriodIndex] != 'break' && listing[currentday][PeriodIndex] != undefined) {
                    //refind the element to highlight
                    var current_period_html = document.getElementById(
                        (
                            "period" +
                            (currentday + 1) +
                            (fakePeriodIndex + 1)
                        ).toString()
                    );
                    var previous_period_html = document.getElementById(
                        (
                            "period" +
                            (currentday + 1) +
                            (fakePeriodIndex)
                        ).toString()
                    );
                    if (previous_period_html != null) {
                        previous_period_html.style.backgroundColor = "#ffffff50";
                    }
                    if (current_period_html != null) {
                        current_period_html.style.backgroundColor = "#0000";
                        time_box.innerHTML =
                            time_box.innerHTML + "<br>" + listing[currentday][PeriodIndex];
                    } else {
                        time_box.innerHTML = time_box.innerHTML + "<br>" + "break";
                    }
                }
                boolean_a = false;
            }
            //check if the period changed
            if (checkPeriod()) {
                boolean_a = true;
            }
            // checking boolean B because we dont want to do the update and the link sending before we finish another tick
            if (boolean_b == true) {
                currentPeriod = listing[currentday][PeriodIndex + 1];
                sound.play();
                if (currentPeriod) {
                    notifyMe("you have : " + currentPeriod + " in 10 mins");
                } else notifyMe("you have : break");
                boolean_b = false;
            }
            // check if its 10 min before the period change
            if (checkPeriod1()) {
                boolean_b = true;
            }
        }
        i++;
        // update the time
        date = new Date();
        refoundDate = new Date(
            date.getFullYear(),
            date.getMonth(),
            date.getDate(),
            date.getHours(),
            date.getMinutes(),
            date.getSeconds(),
            0);
    }, 1000);
}

// check if the user presses CTRL + SHIFT + Z to open the web pages
// function is made by anonyms user, tweked to fit in my use case
var map = {}; // You could also use an array
onkeydown = onkeyup = function (e) {
    e = e || event; // to deal with IE
    map[e.keyCode] = e.type == 'keydown';
    if (map[90]){
    }
    /* insert conditional here */
    if (map[17] && map[16] && map[90]) { // CTRL+SHIFT+Z
        print("hey")
        // CTRL+SHIFT+A
        if (currentPeriod) {
            tab2(currentPeriod);
        }
        map = []
    }
};

/**
 * function for showing the user the dialog, and notifing him if he isnt focused on the tab each 4 seconds
 * @param {String} url1 1st link to use
 * @param {String} url2 2nd link to use
 * @param {String} url3 3rd link to use
 */
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
            win1 = openInNewTab(url1, "1");
            win3 = openInNewTab(url3, "3");
            win2 = openInNewTab(url2, "2");
            if (win2)
                win2.focus();
        }
        // each 4 seconds we ping the user, and retry to see if he focused
    } else setTimeout(() => {
        sound.play()
        tabs(url1, url2, url3)
    }, 4000); //4000ms
}

// finding the period index
function Check_Period_Now(time) {
    for (var key in timing_dictionary) {
        var s = timing_dictionary[key].split(":");
        var dt1 = new Date(
            time.getFullYear(),
            time.getMonth(),
            time.getDate(),
            parseInt(s[0]),
            parseInt(s[1]),
            0
        );
        var dt2 = new Date(
            time.getFullYear(),
            time.getMonth(),
            time.getDate(),
            parseInt(s[2]),
            parseInt(s[3]),
            0
        );
        if (time >= dt1 && time <= dt2) return key;
    }
}

// checking if the period is going to start in 10 min
function checkPeriod1() {
    for (var key in timing_dictionary) {
        if (listing[new Date().getDay()][key] != 'break') {
            date = new Date(
                refoundDate.getFullYear(),
                refoundDate.getMonth(),
                refoundDate.getDate(),
                refoundDate.getHours(),
                refoundDate.getMinutes(),
                refoundDate.getSeconds(),
                0
            );
            s = timing_dictionary[key].split(":");
            dt1 = new Date(
                refoundDate.getFullYear(),
                refoundDate.getMonth(),
                refoundDate.getDate(),
                parseInt(s[0]),
                parseInt(s[1]) - 10,
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
    for (var key in timing_dictionary) {
        date = new Date(
            refoundDate.getFullYear(),
            refoundDate.getMonth(),
            refoundDate.getDate(),
            refoundDate.getHours(),
            refoundDate.getMinutes(),
            refoundDate.getSeconds(),
            0
        );
        s = timing_dictionary[key].split(":");
        var dt2 = new Date(
            refoundDate.getFullYear(),
            refoundDate.getMonth(),
            refoundDate.getDate(),
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

// update the authuser var when changing the input
function authuserChange() {
    authuser = document.getElementById("authuser").value
}