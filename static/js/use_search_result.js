$(document).ready(function () {
    $('.search-results').on('click', function (e) {
        let search_txt = e.currentTarget.innerHTML
        window.location = '/search/?search_field=' + search_txt
    })
});