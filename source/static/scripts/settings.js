var settingsPopup   = document.getElementById("settingsPopup");
var settingsButton  = document.getElementById("buttonSettings");
var settingsContent = document.getElementById("settingsContent");

settingsButton.onclick = function() {
    settingsPopup.style.display = "block";
}

window.onclick = function(event) {
    if (event.target == settingsPopup){
        settingsPopup.style.display = "none";
    }
}



