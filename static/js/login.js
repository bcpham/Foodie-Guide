'use strict';


//console.log('reached login.js')
const loginButton = document.querySelector('#login');

loginButton.addEventListener('submit', (evt) => {
    evt.preventDefault();
//console.log("hi")
    const formInputs = {
      email: document.querySelector('#email').value,
      password: document.querySelector('#password').value,
    };
    
    //console.log(formInputs)

    fetch('/login', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    //Response is from the server
    .then(response => response.text())
    .then(status => {
      
      if (status == "False") {
        document.querySelector('#stat-message').innerHTML = 'The email or password you entered was incorrect.';
    } else {
        document.querySelector('#stat-message').innerHTML = `Currently logged in as ${email.value}!`;
        document.querySelector('#login').hidden = true;
        // document.querySelector('#create-account-link').hidden = true;
        document.querySelector('#logout').hidden = false;
        // document.querySelector('#my-faves').hidden = false; 
        document.querySelector('#my-faves').innerHTML = 'bookmarks'; 
        document.querySelector('#newuser').hidden = true;
    };
  });
});    

