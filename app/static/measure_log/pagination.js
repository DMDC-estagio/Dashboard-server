window.addEventListener("load", function(event) {
  const total_pages = document.getElementById("total_pages").innerHTML;
  const current_page = document.getElementById("current_page").innerHTML;

  var previous = document.getElementById("previous_page");
  var next = document.getElementById("next_page");

  console.log(previous, next)
  console.log(total_pages, current_page)

  if(current_page == 1) {
    previous.classList.add("isDisabled");
    previous.setAttribute("href", "/logs");
  }
  if(current_page == total_pages) {
    next.classList.add("isDisabled");
    next.setAttribute("href", "/logs");
  }

});