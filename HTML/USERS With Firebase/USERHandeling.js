// Import the functions you need from the SDKs you need
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

import {
    initializeApp
} from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-app.js'
import {
    getAuth
} from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-auth.js'
import {
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword
} from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-auth.js'
// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDN_i6hYFN6t1ywJkGuDBmHslbxcuug3SA",
    authDomain: "time-table-reminder.firebaseapp.com",
    databaseURL: "https://time-table-reminder.firebaseio.com",
    projectId: "time-table-reminder",
    storageBucket: "time-table-reminder.appspot.com",
    messagingSenderId: "53486922153",
    appId: "1:53486922153:web:61e96338b619a39de97cb8"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();

// USERHandeling.js
// ========
function makeUserUsingEmailPass(email, password) {
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 
            const user = userCredential.user;
            console.log(user)
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            // ..
        });
}
function signInUsingEmailPass (email, password) {
    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 
            const user = userCredential.user;
            console.log(user)
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
        });
}
