$(function() {
  function isValidEmail(email) {
    var re = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
    return re.test(email);
  }

  function isValidPassword(pwd) {
    // at least one number, one lowercase, one uppercase letter, one special symbol
    // at least nine characters
    var re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[?!_#%^&@-]).{9,}/;
    return re.test(pwd);
  }

  function passwordMatch(password, passwordconfirm){
    //password must match passwordconfirm
    if(password == passwordconfirm){
	return 1;
    }
    else{
	return 0;
    }

  }

  $('#user-add-form').on('submit', function(event) { // form id

    var email = $('#user-email-input').val(); // input id
    var pwd = $('#user-password-input').val(); // input id
    var passwordconfirm = $('#user-passwordconfirm-input').val(); // input id
   
    if( !isValidEmail(email)) {
      alert('Email must be in the correct format.');
      event.preventDefault();
    }

    if( !isValidPassword(pwd)) {
      alert('Password has to be 9 or more characters, and contain at least 1 upper case, 1 lower case, 1 number, and 1 symbol.');
      event.preventDefault();
    }

    if(passwordMatch(pwd, passwordconfirm)) {
      alert('Password does not match password confirmation entry.');
      event.preventDefault();
    }

  });
});