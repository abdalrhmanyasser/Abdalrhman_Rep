// global vars
var refoundDate;
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
var booleb;
var authuser = 1;
var openform = false;
var signed_in = false;
var sound;
// var for sidebar
var mini = true;
var PeriodIndex = 0;
// Client ID and API key from the Developer Console
var CLIENT_ID = '53486922153-8rhm1bn76auo7hdd63gst568hlvqe6vj';
var API_KEY = 'AIzaSyDN_i6hYFN6t1ywJkGuDBmHslbxcuug3SA';

// Array of API discovery doc URLs for APIs used by the quickstart
var DISCOVERY_DOCS = ["https://www.googleapis.com/discovery/v1/apis/classroom/v1/rest"];

// Authorization scopes required by the API; multiple scopes can be
// included, separated by spaces.
var SCOPES =
    "https://www.googleapis.com/auth/classroom.courses https://www.googleapis.com/auth/classroom.courses.readonly";
// get the buttons
var authorizeButton = document.getElementById('authorize_button');
var signoutButton = document.getElementById('signout_button');

// these are the periods in a two dimentional array
// possibility for changing this dynamically through requesting it from the realtime database
var listing = [
    ['English', 'Math', 'ESS', 'Electives', 'Science', 'Arabic', 'Islamic'],
    ['Math', 'ESS', 'Math', 'Electives', 'English', 'Science', 'Arabic'],
    ['English', 'Arabic', 'Science', 'Electives', 'Math', 'ESS', 'Moral_Education'],
    ['English', 'Science', 'Math', 'Electives', 'Islamic', 'ESS', 'Arabic'],
    ['English', 'ESS', 'Science', 'Arabic', 'Math', 'English', 'Islamic']
];

//this dictionary holds the times for the periods start
// possibility for changing this dynamically through requesting it from the realtime database
var timing_dictionary = {
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


// notification sound loading, before the website starts up
function preload() {
    sound = new Audio(
        "ES_Beep%20Tone%20Signal%2054%20-%20SFX%20Producer.mp3"
    );
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
            var url2 = "https://readtheory.org/app/student/quiz";
            var url3 = "https://meet.google.com/lookup/ct4xgqea53?authuser=" + authuser + "&hs=179"; //google Meet
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

// function happens when all functions are made and done
function setup() {
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
        var time = parseInt(
            refoundDate.getHours().toString() +
            (refoundDate.getMinutes().toString().length == 2 ?
                refoundDate.getMinutes().toString() :
                "0" + refoundDate.getMinutes().toString())
        );
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
            refoundDate.getMinutes().toString() +
            ":" +
            secs;
        PeriodIndex = Check_Period_Now(refoundDate);
        // checking if the day is 5 friday or 6 saterday, because there is no need to update on the weekend
        if (currentday != 5 && currentday != 6) {

            PeriodIndex -= 1;
            // find document element to highlight
            var current_period_html = document.getElementById(
                (
                    "period" +
                    (currentday + 1) +
                    (PeriodIndex + 1)
                ).toString()
            );
            // coloring the above found element
            if (current_period_html != null) {
                current_period_html.style.backgroundColor = "#0000";
                time_box.innerHTML =
                    time_box.innerHTML + "<br>" + listing[currentday][PeriodIndex];
            } else {
                time_box.innerHTML = time_box.innerHTML + "<br>" + "break";
            }
            //finding the current period
            currentPeriod = listing[currentday][PeriodIndex];
            // checking boolean A because we dont want to do the update and the link sending before we finish another tick
            if (boolea == true) {
                if (currentPeriod) {
                    sound.play();
                    notifyMe("you have : " + currentPeriod);
                    tab2(currentPeriod);
                } else {
                    //checking if it the end of the day
                    var dt1 = new Date(
                        refoundDate.getFullYear(),
                        refoundDate.getMonth(),
                        refoundDate.getDate(),
                        14,
                        0,
                        1,
                        0
                    );
                    if (dt1.getTime() == refoundDate.getTime()) {
                        tab2("n/a")
                    };
                }
                //refind the element to highlight
                var current_period_html = document.getElementById(
                    (
                        "period" +
                        (currentday + 1) +
                        (PeriodIndex + 1)
                    ).toString()
                );
                var previous_period_html = document.getElementById(
                    (
                        "period" +
                        (currentday + 1) +
                        (PeriodIndex)
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
                boolea = false;
            }
            //check if the period changed
            if (checkPeriod()) {
                boolea = true;
            }
            // checking boolean B because we dont want to do the update and the link sending before we finish another tick
            if (booleb == true) {
                currentPeriod = listing[currentday][PeriodIndex + 1];
                sound.play();
                if (currentPeriod) {
                    notifyMe("you have : " + currentPeriod + " in 10 mins");
                } else notifyMe("you have : break");
                booleb = false;
            }
            // check if its 10 min before the period change
            if (checkPeriod1()) {
                booleb = true;
            }
        }
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

// check if the user presses CTRL + SHIFT + A to open the web pages
// function is made by anonyms user, tweked to fit in my use case
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
    }, 4000);//4000ms
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

        var e = timing_dictionary[key].split(":");
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

// checking if the period is going to start in 10 min
function checkPeriod1() {
    for (var key in timing_dictionary) {
        if (key != 5 || key != 7) {
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

// open the personalized page and close it
function switchForm() {
    if (!openform) {
        document.getElementById("myForm").style.display = "block";
        document.getElementById("wrapper").style.display = "none";
        document.getElementById("personalised").style.display = "block";
        openform = true
    } else {
        openform = false
        document.getElementById("myForm").style.display = "none";
        document.getElementById("wrapper").style.display = "grid";
        document.getElementById("personalised").style.display = "none";
    }
}
// this is the personalized stuff
// sign in, function made by Google inc. adapted to fit my use case
function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    signed_in = true
    document.getElementById("Greetings").innerHTML = "Hello " + profile.getName()
    document.getElementById("Greetings_email").innerHTML = "Email : " + profile.getEmail()
    document.getElementById("signout_button").style.display = "inline-block"
}

// sign out, function made by Google inc. adapted to fit my use case
function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        signed_in = false
        document.getElementById("Greetings").innerHTML = "Hello There"
        document.getElementById("Greetings_email").innerHTML = "sign in to see all data"
        document.getElementById("signout_button").style.display = "none"
    });
}

// closing the sign in form 
function closeForm() {
    document.getElementById("myForm").style.display = "none";
    document.getElementById("openFormBtn").style.display = "inline-block";
}

// opening the sign in form 
function openForm() {
    document.getElementById("myForm").style.display = "block";
    document.getElementById("openFormBtn").style.display = "none";
}


/**
 *  On load, called to load the auth2 library and API client library.
 */
function handleClientLoad() {
    gapi.load('client:auth2', initClient);
}

/**
 *  Initializes the API client library and sets up sign-in state
 *  listeners.
 */
function initClient() {
    gapi.client.init({
        apiKey: API_KEY,
        clientId: CLIENT_ID,
        discoveryDocs: DISCOVERY_DOCS,
        scope: SCOPES
    }).then(function () {
        // Listen for sign-in state changes.
        gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);

        // Handle the initial sign-in state.
        updateSigninStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
        authorizeButton.onclick = handleAuthClick;
        signoutButton.onclick = handleSignoutClick;
    }, function (error) {
        appendPre(JSON.stringify(error, null, 2));
    });
}

/**
 *  Sign in the user upon button click.
 */
function handleAuthClick(event) {
    gapi.auth2.getAuthInstance().signIn();
}

/**
 *  Sign out the user upon button click.
 */
function handleSignoutClick(event) {
    gapi.auth2.getAuthInstance().signOut();
}

/**
 * Append a pre element to the body containing the given message
 * as its text node. Used to display the results of the API call.
 *
 * @param {string} message Text to be placed in pre element.
 */
function appendPre(message, i) {
    var pre = document.getElementById('content');
    var div = document.createElement("div");
    div.className = "row0 column" + String(i)
    div.innerText = message
    div.style =
        "border: 1px solid #00000060;border-radius: 10px;background-color: #ffffff50;padding: 1em;text-align: center;color: #000000;height:75px; width:200px;"
    pre.appendChild(div);
}
/**
 * Append a pre element to the body containing the given message
 * as its text node. Used to display the results of the API call.
 *
 * @param {string} message Text to be placed in pre element.
 * @param {string} link to be used with in the elemenet
 * @param {int} j to be used to identify where to put the cell
 * @param {int} i to be used to identify where to put the cell
 * @param {string} state used to know the state of the classwork
 * @param {boolean} late if true, we make the cell in red
 */
function appendPreLink(message, Link, j, i, state, late) {
    var pre = document.getElementById('content');
    var textContent = document.createTextNode('\n');
    var a = document.createElement('a');
    var div = document.createElement("div");
    if (i == 10) {
        a.className = "row" + String(j + 1) + " columnA"
    } else if (i == 11) {
        a.className = "row" + String(j + 1) + " columnB"
    } else if (i == 12) {
        a.className = "row" + String(j + 1) + " columnC"
    } else {
        a.className = "row" + String(j + 1) + " column" + String(i)
    }
    console.log(state, typeof (state))
    if (state == "TURNED_IN" || state == "RETURNED") {
        div.style.backgroundColor = "#00ff00"
        console.log("turned in / returned")
    } else if (state != "TURNED_IN" && state != "RETURNED" && late == true) {
        div.style.backgroundColor = "#ff0000"
        console.log("missing")
    } else if (state = "NEW" || state == "CREATED") {
        div.style.backgroundColor = "#ffff00"
        console.log("new assignment")
    }
    div.style =
        "border: 1px solid #00000060;border-radius: 10px;padding: 1em;text-align: center;color: #000000;height:75px; width:200px;background-color: " +
        div.style.backgroundColor + ";"
    var span = document.createElement('span');
    var linkText = document.createTextNode(message);
    span.appendChild(linkText);
    div.appendChild(span)
    a.href = "#";
    a.onclick = function _() {
        open(Link)
    }
    span.style = "font-size: 15px;color: #000000;";
    a.appendChild(div)
    pre.appendChild(a)
    pre.appendChild(textContent);
}

/**
 * list all courses
 * we make them in cells, in a grid pattern
 * 3 google classroom api calls
 */
async function listCourses() {
    var courses_with_id = {};
    var courses_with_thingy = {};
    document.getElementById('content').innerHTML = "";
    gapi.client.classroom.courses.list({
        pageSize: 50
    }).then(function (response) {
        var courses = response.result.courses;
        var courses_num = courses.length
        if (courses_num > 0) {
            for (i = 0; i < courses_num; i++) {
                var course = courses[i];
                var id = course.id
                if (course.courseState != "ARCHIVED") {
                    courses_with_id[id] = i
                    appendPre(course.name, i)
                    gapi.client.classroom.courses.courseWork.list({
                        "courseId": course.id,
                        "courseWorkStates": [
                            "PUBLISHED"
                        ],
                        "pageSize": 10
                    }).then(function (response1) {
                            // Handle the results here (response.result has the parsed body).
                            if (response1.result.courseWork) {
                                for (var j = 0; j < response1.result.courseWork.length; j++) {
                                    var newcourseID = response1.result.courseWork[j].courseId
                                    var newcourseWorkID = response1.result.courseWork[j].id
                                    courses_with_thingy[newcourseWorkID] = j
                                    gapi.client.classroom.courses.courseWork.studentSubmissions
                                        .list({
                                            "courseId": newcourseID,
                                            "courseWorkId": newcourseWorkID,
                                            "pageSize": 1
                                        })
                                        .then(function (response2) {
                                                // Handle the results here (response.result has the parsed body).
                                                console.log(response2)
                                                console.log(response2.result.studentSubmissions[
                                                    0].courseWorkId)
                                                k = courses_with_thingy[response2.result
                                                    .studentSubmissions[0].courseWorkId]
                                                var new_i = parseInt(courses_with_id[response1
                                                    .result
                                                    .courseWork[k].courseId])
                                                appendPreLink(response1.result.courseWork[k]
                                                    .title + "\n" + (response2.result
                                                        .studentSubmissions[0]
                                                        .assignedGrade == undefined ? "" :
                                                        response2.result.studentSubmissions[
                                                            0].assignedGrade), (
                                                        response1
                                                        .result.courseWork[k].alternateLink)
                                                    .slice(0,
                                                        28) + "/u/" + authuser + "/" + (
                                                        response1
                                                        .result.courseWork[k].alternateLink)
                                                    .slice(29, (
                                                        response1
                                                        .result.courseWork[k]
                                                        .alternateLink).length), k,
                                                    new_i, response2.result
                                                    .studentSubmissions[0].state, response2
                                                    .result
                                                    .studentSubmissions[0].late)
                                            },
                                            function (err) {
                                                console.error("Execute error", err);
                                            });

                                }
                            }
                        },
                        function (err) {
                            console.error("Execute error", err);
                        });
                } else {
                    courses.splice(i, 1)
                    i--
                    courses_num--
                }
            }
        } else {
            appendPre('No courses found.');
        }
    });
}