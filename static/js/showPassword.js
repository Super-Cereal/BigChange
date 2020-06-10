let password = document.querySelectorAll('.password');
let showPassword = document.querySelectorAll('.show-password');

for (let i = 0; i < password.length; i++) {
  showPassword[i].onchange = function () {
    if (showPassword[i].checked) {
      password[i].type = 'text'
    } else {
      password[i].type = 'password'
    }
  };
}
