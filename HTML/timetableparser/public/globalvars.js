// global vars
var refoundDate;
var currentPeriod = "";
var currentday;
var date;
var s;
var profile;
var win1;
var win3;
var win2;
var url1;
var url3;
var url2;
var dt1;
var boolean_a;
var boolean_b;
var authuser = 2;
var openform = false;
var signed_in = false;
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

// these are the periods in a two dimentional array
// possibility for changing this dynamically through requesting it from the realtime database
var listing = [
    ['English', 'Electives', 'Arabic', 'Science_Block_9-12', 'break', 'English', 'break', 'Math', 'Social_Sciences'],
    ['Electives', 'Math', 'Arabic', 'Science_Block_9-12', 'break', 'English', 'break', 'Social_Sciences', 'Moral_Education'],
    ['Math', 'Math', 'Electives', 'Social_Sciences', 'break', 'Science_Block_9-12', 'break', 'English', 'Islamic'],
    ['Arabic', 'English', 'Electives', 'Science_Block_9-12', 'break', 'Islamic', 'break', 'Social_Sciences', 'Math'],
    ['English', 'Arabic', 'Electives', 'Science_Block_9-12', 'break', 'Islamic', 'break', 'Social_Sciences', 'Math']
];

var Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

var fakePeriodIndex;

//this dictionary holds the times for the periods start
// possibility for changing this dynamically through requesting it from the realtime database
var timing_dictionary = {
    "1": "08:00:08:40",
    "2": "08:45:09:25",
    "3": "09:30:10:10",
    "4": "10:15:10:55",
    "5": "11:00:11:40",
    "6": "11:45:12:25",
    "7": "12:25:12:35",
    "8": "12:35:13:15",
    "9": "13:15:13:55"
};
