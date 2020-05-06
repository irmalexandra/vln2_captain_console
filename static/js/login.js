$(document).ready(function () {
    $('#login-button').on('click', function (e) {
    var username = $.trim($('#id_username').val());
    var pwd = $.trim($('#id_password').val());
    $.ajax({
        url : "/users/login",
        data : {
            username: username,
            pwd : pwd
        }
    }).done(function(data) {
        if (data == "loggedin") {
            window.location = window.location;
        }
        else if (data == "badcredentials") {
            console.log("im here")
            document.getElementById('login-error').style.display = "block"

        }
    });
    })
})
