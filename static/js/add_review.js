$(document).ready(function () {
    $('#review-button').on('click', function (e) {
        let recommend
        var yes = document.getElementById('id_recommend_0').value
        var no = document.getElementById('id_recommend_1').value
        console.log(yes)
        console.log(no)
        if (yes == 'True'){
            console.log("im in yes")

            recommend = yes
        }
        if (no == 'True'){
            console.log("im in no")
            recommend = no
        }
        console.log(recommend)
        var feedback = $.trim($('#id_feedback').val());
        var datetime = $.trim($('#id_datetime').val());
        var product_id = document.getElementById('product_id').innerHTML

        let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
        $.ajax({
            headers: { "X-CSRFToken": csrf_token },
            url : "/games/add_review",
            type: "POST",
            data : {
                feedback: feedback,
                recommend : recommend,
                datetime: datetime,
                product_id: product_id
            }
        }).done(function(data) {
            window.location = window.location;

        });
     })

})