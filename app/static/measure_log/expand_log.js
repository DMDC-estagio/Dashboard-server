function expand_log(e) {
  var others = document.getElementsByClassName(e.className);
  console.log(others);
  for(var i of others) {
    if(i != e) {
      i.classList.remove('expanded');
    }
  }

  e.classList.toggle('expanded');
}