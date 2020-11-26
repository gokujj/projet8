(function ($) {
    "use strict"; // Start of use strict

    $('.search-form input').autocomplete({
        source: AUTOCOMPLETE_PRODUCTS_URL,
        minLength: 2
    });

})(jQuery); // End of use strict
