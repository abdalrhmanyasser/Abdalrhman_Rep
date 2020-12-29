function preload(){
    fajr_sound = loadSound("038-1.mp3");
    othersalat_sound = loadSound("074-1_-.mp3");
}
function setup() {
    let Fajr_replacement;
    let Dhuhr_replacement
    let Sunrise_replacement
    let Asr_replacement
    let Maghrib_replacement
    let Isha_replacement
    const api_url = "http://api.aladhan.com/v1/timingsByCity?city=Dubai&country=United%20Arab%20Emirates&method=8";
    async function get_apiData() {
        const response = await fetch(api_url);
        const Data = await response.json();
        console.log(Data);
        let timings = Data.data.timings;
        console.log(timings);
        let {
            Asr,
            Dhuhr,
            Fajr,
            Isha,
            Maghrib,
            Sunrise,
        } = timings;
        Asr += " AM"
        Dhuhr += " AM"
        Sunrise += " AM"
        Maghrib += " AM"
        Fajr += " AM"
        Isha += " AM"
        if (Asr[0] + Asr[1] >= 12) {
            let i = Asr[0] + Asr[1];
            i = i - 12;
            Asr = nf(i, 2) + Asr[2] + Asr[3] + Asr[4] + ' PM';
        }
        if (Dhuhr[0] + Dhuhr[1] >= 12) {
            let i = Dhuhr[0] + Dhuhr[1];
            i = i - 12;
            Dhuhr = nf(i, 2) + Dhuhr[2] + Dhuhr[3] + Dhuhr[4] + ' PM';
        }
        if (Fajr[0] + Fajr[1] >= 12) {
            let i = Fajr[0] + Fajr[1];
            i = i - 12;
            Fajr = nf(i, 2) + Fajr[2] + Fajr[3] + Fajr[4] + ' PM';
        }
        if (Dhuhr[0] + Dhuhr[1] == 00) {
            i = 12;
            Dhuhr = nf(i, 2) + Dhuhr[2] + Dhuhr[3] + Dhuhr[4] + ' PM';
        }
        if (Isha[0] + Isha[1] >= 12) {
            let i = Isha[0] + Isha[1];
            i = i - 12;
            Isha = nf(i, 2) + Isha[2] + Isha[3] + Isha[4] + ' PM';
        }
        if (Maghrib[0] + Maghrib[1] >= 12) {
            let i = Maghrib[0] + Maghrib[1];
            i = i - 12;
            Maghrib = nf(i, 2) + Maghrib[2] + Maghrib[3] + Maghrib[4] + ' PM';
        }
        if (Sunrise[0] + Sunrise[1] >= 12) {
            let i = Sunrise[0] + Sunrise[1];
            i = i - 12;
            Sunrise = nf(i, 2) + Sunrise[2] + Sunrise[3] + Sunrise[4] + ' PM';
        }
        Fajr_replacement = Fajr
        Dhuhr_replacement = Dhuhr
        Sunrise_replacement = Sunrise
        Asr_replacement = Asr
        Maghrib_replacement = Maghrib
        Isha_replacement = Isha
        let date = Data.data.date.gregorian.date;
        let title = document.getElementById("title")
        title.innerHTML = date + " :توقيت الصلوات ليوم"
        let b1 = document.getElementById("1-b")
        b1.innerHTML = Fajr
        let b2 = document.getElementById("2-b")
        b2.innerHTML = Sunrise
        let b3 = document.getElementById("3-b")
        b3.innerHTML = Dhuhr
        let b4 = document.getElementById("4-b")
        b4.innerHTML = Asr
        let b5 = document.getElementById("5-b")
        b5.innerHTML = Maghrib
        let b6 = document.getElementById("6-b")
        b6.innerHTML = Isha
    }
    get_apiData()
    pdate = new Date();
    setInterval(function () {
        var date = new Date();
        if (checkDate(Fajr_replacement)) {
            fajr_sound.play();
        }
        if (checkDate(Dhuhr_replacement) || checkDate(Asr_replacement) || checkDate(Maghrib_replacement) ||
            checkDate(Isha_replacement)) {
            othersalat_sound.play();
        }
        if (pdate.getDay() != date.getDay()){
            get_apiData()
        }else pdate = new Date()
    }, 1000)
}
function checkDate(time) {
    var date = new Date();
    if (date.getHours() === int(time[0] + time[1]) + 12 && date.getMinutes() === int(time[3] + time[4]) && date.getSeconds() <= 10) {
        return true;
    }
}