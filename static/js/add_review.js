$(document).ready(function () {
    $('#review-button').on('click', function (e) {
        console.log("im in review js")
        var rating = $.trim($('#id_rating').val());
        var feedback = $.trim($('#id_feedback').val());
        var datetime = $.trim($('#id_datetime').val());
        var product_id = document.getElementById('product_id').innerHTML
        console.log("THIS IS product ID", product_id)

        let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
        $.ajax({
            headers: { "X-CSRFToken": csrf_token },
            url : "/games/add_review",
            type: "POST",
            data : {
                feedback: feedback,
                rating : rating,
                datetime: datetime,
                product_id: product_id
            }
        }).done(function(data) {
            window.location = window.location;

        });
     })

})