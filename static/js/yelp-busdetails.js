'use strict';


//Set up mapping for converting raw data from Yelp Fusion API for readability
let daysOfTheWeek = { 0: "Monday", 
                        1: "Tuesday", 
                        2: "Wednesday", 
                        3: "Thursday", 
                        4: "Friday", 
                        5: "Saturday", 
                        6: "Sunday",
                      };

const searchForm = document.querySelector('#search-form');

searchForm.addEventListener('submit', (evt) => {
    evt.preventDefault();
    //The 2 queries below are to make <ul> and <ol> elements empty
    document.querySelector('#yelp-bus-hours').innerHTML = '';
    document.querySelector('#yelp-rev').innerHTML = '';

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

    .then(response => response.json())
    .then(details => {
      
      //VARIOUS SECTIONS THAT DON'T NEED ITERATION
      let name = details['name'];
      let address = details['location']['display_address'];
      
      let phone = details['phone'];
      if (phone.length == 0)
        phone = 'N/A';
    
      let rating = details['rating'];
      let review_count = details['review_count'];
      let yelp_url = details['url'];
      
      //Create hmtl elements and insert into the dom
      document.querySelector('#title-results').innerHTML = 'Results:';
      document.querySelector('#yelp-pic1').src = details['photos'][0];
      document.querySelector('#yelp-pic1').style="height: 300px;";
      document.querySelector('#yelp-pic2').src = details['photos'][1];
      document.querySelector('#yelp-pic2').style="height: 300px;";
      document.querySelector('#yelp-pic3').src = details['photos'][2];
      document.querySelector('#yelp-pic3').style="height: 300px;";
      document.querySelector('#yelp-name').innerHTML = 'Name: ' + name;
      document.querySelector('#yelp-address').innerHTML = 'Address: ' + address;
      document.querySelector('#yelp-phone').innerHTML = 'Phone: ' + phone;
      document.querySelector('#yelp-rating').innerHTML = 'Rating: ' + rating;
      document.querySelector('#yelp-rev-count').innerHTML = 'Total Reviews: ' + review_count;
      
      document.querySelector('#yelp-pro').setAttribute("href", yelp_url);
      document.querySelector('#yelp-pro').innerHTML= "View Yelp profile";
      //END OF VARIOUS SECTIONS

      //BOOKMARK SECTION
      //Reveals "Bookmark this restaurant" button after restaurant search
      //These values are hidden from the homepage.html
      document.querySelector('#rest-fave').removeAttribute("hidden");
      //Populate hidden favorites form with ID
      document.querySelector('#hidden-rest-id').value = details['id']; 
      document.querySelector('#hidden-rest-name').value = name;
      //END OF BOOKMARK SECTION




      //BUSINESS HOURS SECTION - NEEDS ITERATION
      //Yelp Fusion API returns time in 24 hour format
      //We need to convert this to 12 hour format for readability

      function timefunc(yelpTime) {
        let ampm = 'AM';
        
        if (yelpTime >= 1200) {
          ampm = 'PM';
        }
        
        if (yelpTime >= 1300){
          yelpTime = (yelpTime - 1200).toString(); //*Need to convert the difference (int) back to str
        }

        if (yelpTime == '0000') {
          yelpTime = '1200';
        }
        
        yelpTime = yelpTime.slice(0, yelpTime.length-2) + ':' + yelpTime.slice(yelpTime.length-2, yelpTime.length) + ' ' + ampm;
        
        return yelpTime;
      }
      
      document.querySelector('#title-opening').innerHTML = 'Business Hours:';
      
      for (const group of details['hours'][0]['open']) {
        document.querySelector('#yelp-bus-hours').insertAdjacentHTML('beforeend', 
                                                                      `<li> ${daysOfTheWeek[group['day']]}: ${timefunc(group['start'])} to ${timefunc(group['end'])}</li>`);
      }
      
      //END OF BUSINESS HOURS SECTION

      //REVIEWS SECTION - NEEDS ITERATION
      let review_text = [];

      for (const group of details['reviews']) {
        review_text.push(group['text']);
      }
      
      document.querySelector('#title-reviews').innerHTML = 'Reviews:';
      for (const idx in review_text) {
        document.querySelector('#yelp-rev').insertAdjacentHTML('beforeend', `<li>${review_text[idx]}</li>`);
      }
      //END OF REVIEWS SECTION

    });
});