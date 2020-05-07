
const NUMBER_OF_PRODUCTS = $("#table-body").children().length- 1
const TABLE_ROWS = $("#table-body").children()
var PRODUCT_IDS = []
var PRODUCTS = {}

for(i = 0; i < NUMBER_OF_PRODUCTS; i++ ){
    let id = TABLE_ROWS[i].childNodes[5].childNodes[1].childNodes[0].id
    PRODUCT_IDS.push(id)
}

update_total = function () {
    let total = 0
    for (i = 0; i < PRODUCT_IDS.length ; i++) {
        let price = document.getElementById("price-" + PRODUCT_IDS[i]).innerHTML
        total += parseInt(price)
    }
    document.getElementById("price-total").innerHTML = total
}
populate_products = function () {
    for (i = 0; i < PRODUCT_IDS.length ; i++) {
        PRODUCTS[PRODUCT_IDS[i]] =
            {
                'id': PRODUCT_IDS[i],
                'price': document.getElementById("price-" + PRODUCT_IDS[i]).innerHTML,
                'quantity':  document.getElementById(PRODUCT_IDS[i]).value
            }
        document.getElementById("price-" + PRODUCT_IDS[i]).innerHTML = PRODUCTS[PRODUCT_IDS[i]]['quantity'] * PRODUCTS[PRODUCT_IDS[i]]['price']
    }
}
populate_products()
update_total()


$(".quantity").focusout(function (e) {
    let quantity = e.currentTarget.value
    let id = e.currentTarget.id

    $.ajax({
        type:'POST',
        async:false,
        url: '/update_cart_items',
        data: {
            id: id,
            quantity: quantity,
        }
    }).done(function (data) {
        if (data === "success") {
            console.log("Cart Updated")
        }
    })

}).change(function (e) {
    let quantity = e.currentTarget.value
    let id = e.currentTarget.id
    document.getElementById("price-" + id).innerHTML = parseInt(quantity) * parseInt(PRODUCTS[id]["price"])
    update_total()
})

$(".remove-button").click(function (e) {
    e.preventDefault()
    let id = e.currentTarget.id

    $.ajax({
        type:'POST',
        async:false,
        url: '/remove_product',
        data: {
            id: id,
        }
    }).done(function (data) {
        if (data === "success") {
            $("#product-row-" + id).remove()
            PRODUCT_IDS.splice(PRODUCT_IDS.indexOf(id),1)
            delete PRODUCTS[id]
            update_total()
        }
    })
})
$("#clear-all").click(function (e) {
    e.preventDefault()

    $.ajax({
        type:'POST',
        async:false,
        url: '/clear_cart'
    }).done(function (data) {
        if (data === "success") {
            console.log("Cart cleared")
            let replacement = document.createElement("h1").innerHTML = "Cart is empty"
            $("#product-table").replaceWith(replacement)
            $("#submit-button").remove()
            PRODUCT_IDS = []
            PRODUCTS = {}
            alert("Cart cleared")
        }
    })

})

$('#submit-button').on('click', function (e) {
    e.preventDefault()

});

