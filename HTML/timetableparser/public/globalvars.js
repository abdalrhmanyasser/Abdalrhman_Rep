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
var authuser = 1;
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
    ['Moral_Education', 'ESS', 'Electives', 'break', 'English', 'Math', 'Arabic', 'Science'],
    ['Islamic', 'ESS', 'Math', 'break', 'English', 'Arabic', 'English', 'Science'],
    ['Arabic', 'Electives', 'Science', 'break', 'English', 'Math', 'Islamic', 'ESS'],
    ['Arabic', 'English', 'Science', 'break', 'Electives', 'Math', 'Islamic', 'ESS'],
    ['English', 'Science', 'Electives', 'break', 'Math', 'ESS', 'Arabic', 'Math']
];

//this dictionary holds the times for the periods start
// possibility for changing this dynamically through requesting it from the realtime database
var timing_dictionary = {
    "1": "09:00:09:30",
    "2": "08:35:10:05",
    "3": "10:10:10:40",
    "4": "10:40:11:10",
    "5": "11:15:11:45",
    "6": "11:50:12:20",
    "7": "12:25:12:55",
    "8": "13:00:13:30"
};