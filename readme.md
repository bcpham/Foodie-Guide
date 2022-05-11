# Project Proposal

Foodie Guide will be a web application that:

1) Gathers information from both Google and Yelp into a 
    dashboard so that users can better evaluate inormation about restaurants. Oftentimes (especially 
    during the pandemic), it has been difficult to rely on a sole source for updated information (like 
    business hours or ratings).

2) Generates a recommended restaurant base on the radius of location, cuisine, that the user selects.

## Technologies Implemented

- Google Places API: https://developers.google.com/maps/documentation/places/web-service/overview
- Yelp Fusion API: https://www.yelp.com/developers/documentation/v3/get_started

## Data Model

Link: https://drive.google.com/file/d/16QfFvefSKAFCE3Mzg08B_r5fPlqjcmN2/view?usp=sharing

## Roadmap

### MVP

1) Log in/out feature to maintain personalized experience (to bookmark restaurants in NTH) 
2) Allowing users to search any restaurant they want, collect information from Yelp to display attributes (for business hours, ratings, etc.) (Form, for user’s input)
3) Display 3 most recent reviews from Yelp (double check parameters)

### 2.0

1) Use javascript/ajax to implement bookmark/favorite restaurants when a user is logged in
2) Incorporate google places
3) If the user is indecisive on which restaurant to go to, 
   there can be a random generator of restaurants in the selected neighborhood that outputs restaurant recommendations.


### Nice-to-haves

1) Potentially to work with local restaurants if they could provide special discounts for Foodie Seattle users
2) Mobile app friendly

image.png