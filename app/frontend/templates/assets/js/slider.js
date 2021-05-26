var slider1 = document.getElementById("beds");
var output1 = document.getElementById("display1");
output1.innerHTML = slider1.value; // Display the default slider value
// Update the current slider value (each time you drag the slider handle)
slider1.oninput = function() {
  output1.innerHTML = this.value;
}


var slider2 = document.getElementById("bedrooms");
var output2 = document.getElementById("display2");
output2.innerHTML = slider2.value;
slider2.oninput = function() {
    output2.innerHTML = this.value;
  }

var slider3 = document.getElementById("bathrooms");
var output3 = document.getElementById("display3");
output3.innerHTML = slider3.value;
slider3.oninput = function() {
    output3.innerHTML = this.value;
}

var slider4 = document.getElementById("accomodates");
var output4 = document.getElementById("display4");
output4.innerHTML = slider4.value;
slider4.oninput = function() {
    output4.innerHTML = this.value;
    }