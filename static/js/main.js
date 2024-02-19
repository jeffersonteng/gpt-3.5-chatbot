var input = document.getElementById("query");
var button = document.getElementById("myButton");
input.addEventListener("keyup", function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    button.click();
  }
});