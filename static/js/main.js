var input = document.getElementById("query");
var button = document.getElementById("myButton");
input.addEventListener("keyup", function(event) {
  console.log(event.key);
  if (event.key === 'Enter') {
    event.preventDefault();
    button.click();
  }
  // if (event.keyCode === 13) {
  //  event.preventDefault();
  //  document.getElementById("mybutton").click();
  // }
});

// let loginForm = document.getElementById("form");

// loginForm.addEventListener("submit", (e) => {
//   e.preventDefault();
//   console.log('submit');

//   let username = document.getElementById("username");
//   let password = document.getElementById("password");

//   if (username.value == "" || password.value == "") {
//     alert("Ensure you input a value in both fields!");
//   } else {
//     // perform operation with form input
//     alert("This form has been successfully submitted!");
//     console.log(
//       `This form has a username of ${username.value} and password of ${password.value}`
//     );

//     username.value = "";
//     password.value = "";
//   }
// });