// this is the personalized stuff
// sign in, function made by Google inc. adapted to fit my use case

// open the personalized page and close it
function switchForm() {
    if (!openform) {
        document.getElementById("wrapper").style.display = "none";
        document.getElementById("personalised").style.display = "block";
        openform = true
    } else {
        openform = false
        document.getElementById("wrapper").style.display = "grid";
        document.getElementById("personalised").style.display = "none";
    }
}

function onSignIn(googleUser) {
    profile = googleUser.getBasicProfile();
    signed_in = true
    document.getElementById("Greetings").innerHTML = "Hello " + profile.getName()
    document.getElementById("Greetings_email").innerHTML = "Email : " + profile.getEmail()
    document.getElementById("signout_button").style.display = "inline-block"
    document.getElementById("myForm").style.display = "none";
    document.getElementById("openFormBtn").style.display = "inline-block";
}

function updateSigninStatus(isSignedIn) {
    if (signed_in) {
        signed_in = true
        document.getElementById("Greetings").innerHTML = "Hello " + profile.getName()
        document.getElementById("Greetings_email").innerHTML = "Email : " + profile.getEmail()
        document.getElementById("signout_button").style.display = "inline-block"
        document.getElementById("myForm").style.display = "none";
        document.getElementById("openFormBtn").style.display = "inline-block";
    } else {
        signed_in = false
        document.getElementById("Greetings").innerHTML = "Hello There"
        document.getElementById("Greetings_email").innerHTML = "sign in to see all data"
        document.getElementById("signout_button").style.display = "none"
        if (document.getElementById("personalised").style.display == "block") {
            document.getElementById("myForm").style.display = "block";
        }
        document.getElementById("openFormBtn").style.display = "none";
    }
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
        //buttons
        var authorizeButton = document.getElementById('authorize_button');
        var signoutButton = document.getElementById('signout_button');
        authorizeButton.onclick = handleAuthClick;
        signoutButton.onclick = handleSignoutClick;
    }, function (error) {
        console.log(JSON.stringify(error));
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
    if (state == "TURNED_IN" || state == "RETURNED") {
        div.style.border = "3px solid #00ff00"
    } else if (state != "TURNED_IN" && state != "RETURNED" && late == true) {
        div.style.border = "3px solid #ff0000"
    } else if (state = "NEW" || state == "CREATED") {
        div.style.border = "3px solid #ffff00"
    }
    div.style =
        "background-color: #ffffff50;border-radius: 10px;padding: 1em;text-align: center;color: #000000;height:75px; width:200px;border: " +
        div.style.border + ";"
    var span = document.createElement('span');
    var linkText = document.createTextNode(message);
    span.appendChild(linkText);
    div.appendChild(span)
    a.onclick = () => {open(Link)}
    span.style = "font-size: 15px;color: #000000;";
    a.appendChild(div)
    pre.appendChild(a)
    pre.appendChild(textContent);
}

/**
 * list all courses
 * we make them in cells, in a grid pattern
 * 3 nested google classroom api calls
 * 1* Number Of courses ^ number of course matirials
 * a lot of google classroom api calls, wish there was a better way
 */
async function listCourses() {
    if (signed_in) {
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
                        console.log(course.name, course.id)
                        gapi.client.classroom.courses.courseWork.list({
                            "courseId": course.id,
                            "courseWorkStates": [
                                "DRAFT",
                                "PUBLISHED",
                                "DELETED"
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
                                                    var submition = response2.result.studentSubmissions[0]
                                                    // Handle the results here (response.result has the parsed body).
                                                    k = courses_with_thingy[submition.courseWorkId]
                                                    var new_i = parseInt(courses_with_id[response1
                                                        .result
                                                        .courseWork[k].courseId])
                                                    appendPreLink(response1.result.courseWork[k]
                                                        .title + (submition
                                                            .assignedGrade == undefined ? "" :
                                                            "\ngrade : " +
                                                            submition
                                                            .assignedGrade), (
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
                                                        new_i, submition.state,
                                                        submition.late)
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
    }else{
        notifyMe("Please Sign in first")
    }
}