'use strict';

const button = document.querySelector('#search-form');

button.addEventListener('submit', (evt) => {
    evt.preventDefault();
    // const url = `https://api.yelp.com/v3/businesses/${business_id}`;

    const formInputs = {
      rname : document.querySelector("#rname").value,
      city  : document.querySelector("#city").value,
    };

  fetch('/restaurant-search',  
    {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    }

    )
    .then(response => response.text())
    .then(status => {
      console.log(status)
      
      //Create hmtl elements and insert into the dom
      document.querySelector('#restaurant-result').innerHTML = status;
    });
});


