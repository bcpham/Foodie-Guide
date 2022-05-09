'use strict';


const editButton = document.querySelector('#edit-mode');

editButton.addEventListener('submit', (evt) => {
    evt.preventDefault();
    
    document.querySelector("#user-favorite").hidden = true;
    document.querySelector("#user-favorite-form").hidden = false;
    document.querySelector("#edit-mode").hidden = true;
});

const cancelButton = document.querySelector('#fav-cancel-button');

cancelButton.addEventListener('click', (evt) => {
    evt.preventDefault();
    
    document.querySelector("#user-favorite").hidden = false;
    document.querySelector("#user-favorite-form").hidden = true;
    document.querySelector("#edit-mode").hidden = false;
}); 

const deleteForm = document.querySelector('#user-favorite-form');

deleteForm.addEventListener('submit', (evt) => {
    evt.preventDefault();

    const formInputs = {
      userFavToDelete: document.querySelector("input[name=favorites]:checked").value,
      rnameToDelete: document.querySelector("input[name=favorites]:checked").id,
    };

    fetch('/delete-favorite', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    .then(response => response.text())
    .then(status => {
        status = JSON.parse(status);
        console.log(status)

        document.querySelector("#user-favorite").hidden = false;
        document.querySelector("#user-favorite-form").hidden = true;
        document.querySelector("#edit-mode").hidden = false;  
        document.querySelector('#stat-message').innerHTML = status["msg"];

        if (status["success"] == true) {
            console.log(`#rest-div-${status["restaurant_id"]}`);
            document.querySelector(`#rest-div-${status["restaurant_id"]}`).remove();
            document.querySelector(`#li-fav-${status["restaurant_id"]}`).remove();
        }
    });
});  