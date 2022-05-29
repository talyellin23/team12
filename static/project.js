//FAQ - opening the explenation after clicking on it
var acc = document.getElementsByClassName("questions");
var i;

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
var acc = document.getElementsByClassName("questions");
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


// registration password and email validation - checking if user is already registered
function validUser() {
  var returnVal = true;
  let firstpassword = document.getElementById("psw").value;
  let secondpassword = document.getElementById("psw_repeat").value;
  let validEmail = document.getElementById("email").value;
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  if (firstpassword == secondpassword) {
    if (re.test(String(validEmail).toLowerCase())) {
      returnVal = true;
    }
    else {
      alert("email is not valid");
      returnVal = false;
    }
  }
  else {
    if (re.test(String(validEmail).toLowerCase())) {
      alert("password must be same!");
      returnVal = false;
    }
    else {
      alert("wrong details!");
    }
  }
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

// popping massege after taking user location
function showPosition(position) {
  var x = document.getElementById("successLocation");
  var y = document.getElementById("LocationBtn");
  x.innerHTML = "Location has been succesfully received"

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
    }
    else {
      ReadMoreButton.innerText = "Click hear to read more";
    }
  })
}

//Validation - all radio items are selected before the submitting of the form
var sub = document.getElementById('submitData')
if (sub) {
  document.getElementById('submitData').onclick = function () {
    var radios = document.getElementsByClassName("radio-item");
    var selected = Array.from(radios).filter(radio => radio.checked);
    if (!selected || selected.length != 4) {
      alert("Please answer all the questions");

    }
    else {
      location.href = "BMIResults.html"; 
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