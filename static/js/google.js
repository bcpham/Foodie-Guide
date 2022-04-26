"use strict";

// Initialize and add the map
function initMap() {
    // The location of Hackbright Academy
    const default_location = { lat:   40.42001810620129, lng: -111.87428871164335 };
    // The map, centered at Hackbright Academy
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 15,
      center: default_location,
    });
    // The marker, positioned at Hackbright Academy
    const marker = new google.maps.Marker({
      position: default_location,
      map: map,
    });
  }
  
  window.initMap = initMap;