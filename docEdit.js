let myFont;
let logo;



function format(command, value) {
    document.execCommand(command, false, value);
}


function preload(){
  myFont=loadFont('orange juice 2.0.ttf');
  logo=loadImage('logo.png');

function setup (){

  image(logo, 375, 300);
  }


function changeFont() {
    const Font = document.getElementById('input-font').value;
    document.execCommand('fontName', false, Font);
}

function changeSize() {
    const size = document.getElementById('fontSize').value;
    document.execCommand('fontSize', false, size);
}
