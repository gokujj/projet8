// Saves a favorite using ajax and the favorites API
function saveFavorite(event, saveButton, deleteButton) {
    event.preventDefault();
    let body = new FormData();
    body.append('product', saveButton.dataset.product);
    body.append('substitute', saveButton.dataset.substitute);
    let url = saveButton.href;
    let headers = {"X-CSRFToken": getCookie('csrftoken')};

    // http requet to the favorites api to create a favorite
    fetch(url, {body, headers, method: 'POST', credentials: 'same-origin'})
    .then(response => response.json())
    .catch(error => console.error(error))
    .then(data => {
        saveButton.classList.toggle('d-none');
        deleteButton.classList.toggle('d-none');
        deleteButton.href = data.url;
    });
}

// Delete a favorite using ajax and the favorites API
function deleteFavorite(event, saveButton, deleteButton) {
    event.preventDefault();
    let url = deleteButton.href;
    let headers = {"X-CSRFToken": getCookie('csrftoken')};

    // sends a delete http request to the favorites API
    fetch(url, {headers, method: 'DELETE', credentials: 'same-origin'})
    .then(response => {
        saveButton.classList.toggle('d-none');
        deleteButton.classList.toggle('d-none');
        deleteButton.href = "#";
    })
    .catch(error => console.error(error));
}

// Main entry point of the stript
(function () {
    "use strict" // Start of use strict

    let substitutes = document.querySelectorAll('.substitute');
    substitutes.forEach(substitute => {
        let saveButton = substitute.querySelector('.substitute__button--save');
        let deleteButton = substitute.querySelector('.substitute__button--delete');
        saveButton.addEventListener('click', event => {
            saveFavorite(event, saveButton, deleteButton);
        });
        deleteButton.addEventListener('click', event => {
            deleteFavorite(event, saveButton, deleteButton);
        });
    });

})(); // End of use strict
