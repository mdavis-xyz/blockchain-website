$(document).ready(function() {
   var $sliderL = document.getElementById('slider-l');
   var $sliderR = document.getElementById('slider-r');
   var $toggle = document.getElementById('toggle');



});

function slide(oldElID,newElID,direction){
   var newEl = document.getElementById(newElID);
   var oldEl = document.getElementById(oldElID);
   console.log(`sliding ${oldElID} to ${direction} to make room for ${newElID} `);
   newEl.scrollTop = 0;
   newEl.setAttribute('class', 'slide-in-' + direction);
   oldEl.setAttribute('class', 'slide-out-' + direction);
}
