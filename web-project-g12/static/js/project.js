//FAQ - opening the explenation after clicking on it
let acc = document.getElementsByClassName("questions");

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}

//FAQ - closing the explenation after clicking on it
acc = document.getElementsByClassName("questions");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}

//location function
function GetLocation() {
    if (navigator.geolocation) {
        console.log("in get location");
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        document.getElementById("successLocation").innerHTML = "Geolocation is not supported by this browser.";
    }
}

// popping massage after taking user location and get coordination to get user region
function showPosition(position) {
    const x = document.getElementById("successLocation");
    const y = document.getElementById("LocationBtn");
    let latitudte = position.coords.latitude
    let longtidute = position.coords.longitude
    console.log(latitudte)
    console.log(longtidute)
    let area = null;
    let bol = true
    x.innerHTML = "Location has been successfully received"
    if (latitudte > 29.493 && latitudte < 29.758)
        area = "Eilat"
    else if (latitudte > 29.758 && latitudte < 31.669)
        area = "South"
    else if (latitudte > 31.669 && latitudte < 32.350 && longtidute < 35.0835)
        area = "Center"
    else if (latitudte > 31.669 && latitudte < 32.350 && longtidute > 35.0835)
        area = "Jerusalem"
    else if (latitudte > 32.350 && latitudte < 33.2839 && longtidute < 35.612)
        area = "North"
    else if (latitudte > 32.687 && latitudte < 33.2839 && longtidute > 35.612)
        area = "Golan Heights"
    console.log(area)
    const request = new XMLHttpRequest()
    request.open('POST', `/ProcessArea/${JSON.stringify(area)}`)
    request.send();
    const loc = new XMLHttpRequest()
    loc.open('POST', `/ProcessBoolean/${JSON.stringify(bol)}`)
    loc.send();
    console.log(position);
}

//BMI - matching the slider value to the number showing next to it
const sliders = document.querySelectorAll('.slider-wrapper');

sliders.forEach(slider => {
    slider.addEventListener('input', () => {
        slider.lastElementChild.innerHTML = slider.firstElementChild.value
    })
})

//Reveal more - click here to read more information
const ReadMoreButton = document.querySelector('.readMoreButton');
const text = document.querySelector('.text');
if (ReadMoreButton) {
    ReadMoreButton.addEventListener('click', (e) => {
        text.classList.toggle('show-more');
        if (ReadMoreButton.innerText == "Click hear to read more") {
            ReadMoreButton.innerText = "Click hear to read less";
        } else {
            ReadMoreButton.innerText = "Click hear to read more";
        }
    })
}

//Validation - all radio items are selected before the submitting of the form
var sub = document.getElementById('submitData')
if (sub) {
    nisuy2 = document.getElementById('resultsExplain')
    console.log(nisuy2)
    document.getElementById('submitData').onclick = function hello() {
        var radios = document.getElementsByClassName("radio-item");
        var selected = Array.from(radios).filter(radio => radio.checked);
        if (!selected || selected.length != 4) {
            alert("Please answer all the questions");

        } else {
            let Weight = document.getElementById("Weight").value
            let Height = document.getElementById("Height").value
            let Age = document.getElementById("Age").value
            let gender = document.getElementsByName("Gender")
            let ifsmoke2 = document.getElementsByName("Answer")
            var selected3 = Array.from(gender).find(radio => radio.checked) //check if man or woman
            var IfSmoke = Array.from(ifsmoke2).find(radio => radio.checked) // check if smoking or not
            console.log(selected3.value)
            console.log(IfSmoke.value)
            var Bmr = 0
            var BmrMen = 88.362 + (13.397 * Weight) + (4.799 * Height) - (5.677 * Age)
            var BmrWomen = 447.593 + (9.247 * Weight) + (3.098 * Height) - (4.33 * Age)
            if (selected3.value == "Male" || selected3.value == "Other") {
                Bmr = BmrMen
                Bmrconv = Number(Bmr.toFixed(2))
                console.log(Bmrconv)
            }
            if (selected3.value == "Female") {
                Bmr = BmrWomen
                Bmrconv = Number(Bmr.toFixed(2))
            }
            console.log(Bmr)
            console.log(BmrMen)
            console.log(BmrWomen)

            var bmi = (Weight / ((Height / 100) ** 2))
            var bmiConve = Number(bmi.toFixed(2))
            console.log(bmi)
            if (bmi <= 18.4 && IfSmoke.value == "Yes")
                Messeage = "You are underwieght. It is recommended to consume more calories per day, so that the body gets all the nutrients it needs.In addition, we noticed that you smoker, so we recommend rehab centers in your area to improve your health."
            if (bmi <= 18.4 && IfSmoke.value == "No") {
                Messeage = "You are underwieght. It is recommended to consume more calories per day, so that the body gets all the nutrients it needs."
            }
            if (bmi >= 18.4 && bmi <= 24.9 && IfSmoke.value == "Yes")
                Messeage = "Well done! Your weight is normal,it means you maintain a healty lifestyle,we recommend to meet our trainers to improve yourself even more.In addition, we noticed that you smoker, so we recommend rehab centers in your area to improve your health."
            if (bmi >= 18.4 && bmi <= 24.9 && IfSmoke.value == "No") {
                Messeage = "Well done! Your weight is normal,it means you maintain a healty lifestyle,we recommend to meet our trainers to improve yourself even more."
            }
            if (bmi >= 25 && bmi <= 29.9 && IfSmoke == "Yes")
                Messeage = "You are over weight.This may be because your daily calorie intake is large relative to the energy your body expends during the day.,we recommend to meet our trainers and nutritionists.In addition, we noticed that you smoker, so we recommend rehab centers in your area to improve your health."
            if (bmi >= 25 && bmi <= 29.9 && IfSmoke == "No") {
                Messeage = "You are over weight.This may be because your daily calorie intake is large relative to the energy your body expends during the day.,we recommend to meet our trainers and nutritionists."
            }
            if (bmi >= 30 && bmi <= 60 && IfSmoke == "Yes") {
                Messeage = "Your weight is significantly higher than the norm. We highly recommend going to one of the doctors from the table below.In addition, we noticed that you smoker, so we recommend rehab centers in your area to improve your health."
            }
            if (bmi >= 30 && bmi <= 60 && IfSmoke == "No") {

                Messeage = "Your weight is significantly higher than the norm. We highly recommend going to one of the doctors from the table below."
            }


            location.href = "BMIResults.html?bmiConve=" + bmiConve + "&Bmrconv=" + Bmrconv + "&Messeage=" + Messeage; //add all meseeges and bmr


        }


    }

}


//Mark which page we are at
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('a').forEach(link => {
    if (link.href.includes(`${activePage}`)) {
        link.classList.add('active');

    }
})
// get location from user according to cordinates





