from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from django.contrib.auth.decorators import login_required
from carts.models import Cart, CartItems
from users.models import Profile

#@login_required(login_url="/users/login")


def index(request):
    class Model:
        name = ""
        quantity = 0
        img = ""
        price = 0

    if request.user.is_authenticated:
        user_id = Profile.objects.filter(user=request.user).first().id
        user_cart = Cart.objects.filter(userID=user_id).first()
        cart = CartItems.objects.filter(cartID=user_cart.id)
        models = []
        price_sum = 0

        for product in cart:
            model = Model()
            model.quantity = product.quantity
            model.price = product.price
            item = Product.objects.filter(id=product.productID).first()
            price_sum += product.price
            model.img = item.product_display_image
            model.name = item.name
            models.append(model)

        context = {
            'price_sum': price_sum,
            'models': models
            }
        return render(request, 'carts/index.html', context)

    else:
        print(request.user)
        print("help")




def cart_add(request, id):
    print(request.session)
    request.session['cartID'] = "yes"
    print(request.session['cartID'])

    if request.user.is_authenticated:
        userID = Profile.objects.filter(user=request.user).first().id
        product = Product.objects.filter(id=id).first()
        userCart = Cart.objects.filter(userID=userID).first()

        if not userCart:
            print("What? new one?")
            userCart = Cart.objects.create(userID=userID, check_out=False)

        CartItems.objects.create(productID=product.id, quantity=1, cartID=userCart, price=product.price)

    else:
        print(request.session.session_key, "<--- Segja Emil frá þessu")
        print("help")

    return redirect(request.GET['next'])


#@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


#@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


#@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


#@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


#@login_required(login_url="/users/login")
def cart_detail(request):

    return render(request, 'carts/order_details.html')