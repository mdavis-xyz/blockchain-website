$(document).ready(function() {
   var $sliderL = document.getElementById('slider-l');
   var $sliderR = document.getElementById('slider-r');
   var $toggle = document.getElementById('toggle');

   $toggle.addEventListener('click', function() {
       var isOpen = $sliderL.classList.contains('slide-in');

       $sliderL.setAttribute('class', isOpen ? 'slider slide-out' : 'slider slide-in');
       $sliderR.setAttribute('class', isOpen ? 'slider slide-in' : 'slider slide-out');
   });
});
