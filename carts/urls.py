from django.urls import path
from . import views

urlpatterns = [
    path('carts/add/<int:id>/', views.cart_add, name='cart_add'),
    path('remove_product', views.remove_product, name='remove_product'),
    path('carts/cart_clear/', views.cart_clear, name='cart_clear'),
    path('carts/', views.index, name="cart-index"),
    path('update_cart_items', views.update_cart_items),
    path('carts/shipping_information', views.shipping_info, name='shipping_info'),

]
