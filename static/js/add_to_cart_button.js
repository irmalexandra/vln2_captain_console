const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value
console.log("hello from add to cart")
$(".alert").hide()
$(document).ready(function () {
    $(".add_to_cart_button").click(function (e) {
        e.preventDefault()
        console.log(Date.now() + 2000)
        let status = document.getElementById("status-"+e.target.id)
        message = document.createElement('p')
        message.className = "alert-link"
        $.ajax({
            headers:{ "X-CSRFToken": csrf_token } ,
            type:'POST',
            url: '/carts/add',
            data: {'id': e.target.id}

        }).done(function (data) {

            if (data) {
                status.style.display = "block"
                if(data == "1"){
                    message.innerText = 'Added to cart'
                }
                else{
                    if(status.childNodes.length > 0){
                        status.removeChild(status.childNodes[0])
                    }

                    message.innerText = 'Added to cart (' + data + ')'
                }

                status.appendChild(message)
                console.log("Cart Updated")
                function sleeper(){
                    $(status).fadeOut(2000)
                }
                setTimeout(sleeper, 1500);
            }
        })
    })
})
