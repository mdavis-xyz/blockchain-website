$(document).ready(function() {
   var $sliderL = document.getElementById('slider-l');
   var $sliderR = document.getElementById('slider-r');
   var $toggle = document.getElementById('toggle');



});

function slide(oldElID,newElID,direction){
   var newEl = document.getElementById(newElID);
   var oldEl = document.getElementById(oldElID);
   console.log(`sliding ${oldElID} to ${direction} to make room for ${newElID} `);
   var newattr = 'slider slide-in-' + direction;
   console.log(`setting attribute to ${newattr}`)
   newEl.setAttribute('class', 'slider slide-in-' + direction);
   oldEl.setAttribute('class', 'slider slide-out-' + direction);
}
