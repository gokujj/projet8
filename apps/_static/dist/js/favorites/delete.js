// Deletes a favorite from the favorites list template
function deleteFavorite(event, favorite, deleteButton) {
    event.preventDefault();
    let url = deleteButton.href;
    let headers = {'X-CSRFToken': getCookie('csrftoken')};

    // http request to delete the favorite using the favorites API
    fetch(url, {headers, method: 'DELETE', credentials: 'same-origin'})
    .then(response => {
        favorite.remove();
        let favorites = document.querySelectorAll('.favorite');
        if (favorites.length == 0) {
            let parent = document.querySelector('.favorites');
            parent.innerHTML = "<p>Vous n'avez enregistré aucun favori !</p>"
        }
    })
    .catch(error => console.log(error));
}

// Main entry point of the stript
(function () {
    "use strict" // Start of use strict

    let favorites = document.querySelectorAll('.favorite');
    favorites.forEach(favorite => {
        let deleteButton = favorite.querySelector('.favorite__button--delete');
        deleteButton.addEventListener('click', event => {
            deleteFavorite(event, favorite, deleteButton);
        })
    });

})(); // End of use strict 
