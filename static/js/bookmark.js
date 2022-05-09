'use strict';


const bookmarkButton = document.querySelector('#rest-fave');

bookmarkButton.addEventListener('submit', (evt) => {
    evt.preventDefault();
    //console.log("hi")
    const formInputs = {
      
      revealed_yelp_rest_id: document.querySelector('#hidden-rest-id').value,
      rname: document.querySelector('#hidden-rest-name').value,

    };
    
    //console.log(formInputs)

    fetch('/add-favorites', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    .then(response => response.text())
    .then(status => {
      
      if (status == "False") {
        document.querySelector('#stat-message').innerHTML = `You must be logged in to bookmark ${rname.value}!`;
    } else if (status == "True") {
        document.querySelector('#stat-message').innerHTML = `You just favorited ${rname.value}!`;
    } else {  
        document.querySelector('#stat-message').innerHTML = `You already favorited ${rname.value}!`;
    }; 
  });
});    

