
var backButton = null;
var navHistory = [];
var navDirections = [];
var currentElID = null; // won't be used until we navigate anyway

function slide(oldElID,newElID,direction){
   slideNoHist(oldElID,newElID,direction);
   if(navHistory.length == 0) {
      document.getElementById("back-button").setAttribute('class', 'left-arrow slide-in-button'); // not hidden
   }
   navHistory.push(oldElID);
   navDirections.push(direction);
}

function slideNoHist(oldElID,newElID,direction){
   var newEl = document.getElementById(newElID);
   var oldEl = document.getElementById(oldElID);
   console.log(`sliding ${oldElID} to ${direction} to make room for ${newElID} `);
   newEl.scrollTop = 0;
   newEl.setAttribute('class', 'slide-in-' + direction);
   oldEl.setAttribute('class', 'slide-out-' + direction);
   currentElID = newElID;
}

function reverseDirection(prevDir){
   var newDir;
   switch(prevDir.toLowerCase()) {
       case 'up':
           newDir = 'down';
           break;
       case 'down':
           newDir = 'up';
           break;
       case 'left':
           newDir = 'right';
           break;
       case 'right':
           newDir = 'left';
           break;
   }
   console.log(`reverse of ${prevDir} is ${newDir}`);
   return(newDir);
}

function back(){
   var newElID = navHistory.pop();
   var direction = reverseDirection(navDirections.pop());
   console.log(`Sliding back from ${currentElID} to ${newElID}`);
   slideNoHist(currentElID,newElID,direction);
   if(navHistory.length == 0) {
      if (backButton == null){
         backButton = document.getElementById('back-button');
      }
      backButton.setAttribute('class', 'left-arrow slide-out-button');
   }
}
