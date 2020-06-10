let password = document.querySelector('.password');
let showPassword = document.querySelector('.show-password');

showPassword.onchange = function () {
  if (showPassword.checked) {
    password.type = 'text'
  } else {
    password.type = 'password'
  }
};

