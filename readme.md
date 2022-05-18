# Project Overview

Work in progress:
![Picture1](https://user-images.githubusercontent.com/100656595/168994805-c1c3dfdf-3946-4b6d-82b2-a6f475c7661e.png)


During the pandemic, it has become difficult to reply on a single source for accurate information about restaurants.
Foodie Guide is a web application that:

1) Gathers information from both Google and Yelp into a 
    dashboard so that users can better evaluate inormation about restaurants.

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
2) Incorporate Google Places
3) If the user is indecisive on which restaurant to go to, 
   there can be a random generator of restaurants in the selected neighborhood that outputs restaurant recommendations.


### Nice-to-haves

1) Potentially to work with local restaurants if they could provide special discounts for Foodie Seattle users
2) Mobile app friendly

![Picture2](https://user-images.githubusercontent.com/100656595/168995903-21b65a5e-c481-45f0-837e-eced3e495456.png)
![Picture3](https://user-images.githubusercontent.com/100656595/168995943-66cf67cf-8fe5-495c-8ea4-0b417759b693.png)
