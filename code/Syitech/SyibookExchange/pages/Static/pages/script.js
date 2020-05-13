var Wsize = window.innerWidth;
var filter = document.getElementsByClassName("filterContainer");
var options = document.getElementById('sideFilter');
var i = 0;

var Hsize = window.innerHeight;
var feed = document.getElementsByClassName("prod_container");

$(document).ready(function(){
  filter_UX_change();
  // newsFeedHeight();
});

function filter_UX_change(){
  // only insert once button once
  if (i < 1){
    // create button for screens under certain number of px
    if (Wsize <= 990) {
      var filterBtn = document.createElement('BUTTON');
      filterBtn.innerHTML = 'Filter';
      filterBtn.type = 'button';
      filterBtn.className = 'btn btn-danger filterBtn';
      filterBtn.id = 'filterBtn';
      filterBtn.setAttribute("data-toggle","collapse");
      filterBtn.setAttribute("data-target","#sideFilter");
      document.getElementById("filterBtn_container").appendChild(filterBtn);
      options.classList.add('collapse');
      i = 1;
    }
  }
  // if screen is resize to be bigger revert the UX change
  // if (Wsize > 990){
  //   document.getElementById("filterBtn_container").remove(filterBtn);
  //   options.classList.remove('collapse');
  //   i = 0;
  // } 
}
