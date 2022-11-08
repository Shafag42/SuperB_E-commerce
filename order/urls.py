from django.urls import path
from .views import checkout_billing_info, checkout, shopping_cart, wishlist
from . import views

app_name = 'basket'

urlpatterns = [
    path('checkout_billing_info/', checkout_billing_info, name='checkout_billing_info'),
    path('checkout/', checkout, name='checkout'),
    path('shopping_cart/',shopping_cart, name='shopping_cart'),
    path("wishlist/", views.wishlist, name="wishlist"),
    # path('wishlist/add_to_wishlist/<int:id>',views.add_to_wishlist, name='user_wishlist'),
    # path('', views.basket_summary, name='basket_summary'),
    # path('add/', views.basket_add, name='basket_add'),  # type: ignore
    # path('delete/', views.basket_delete, name='basket_delete'),  # type: ignore
    # path('update/', views.basket_update, name='basket_update'),  # type: ignore

]