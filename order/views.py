from django.shortcuts import render, get_object_or_404, render
from django.http import JsonResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from .models import Order, OrderItem,Basket, WishList
from product.models import product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required
def wishlist(request):
    products = WishList.objects.filter(user=request.user).all()
    return render(request, "wishlist.html", {"wishlist": products})


# @login_required
# def add_to_wishlist(request, id):
#     Product=get_object_or_404(product,id=id)
#     if Product.users_wishlist.filter(id=request.user.id).exists():
#         Product.users_wishlist.remove(request.user)
#         messages.success(request, f"{product.name} has been removed from your WishList")

#     else:
#         Product.users_wishlist.add(request.user)
#         messages.success(request, f"Added {product.name} to your WishList")
#     return HttpResponseRedirect(request.META["HTTP_REFERER"])
    


# def add(request):   # sourcery skip: remove-pass-body
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':

#         order_key = request.POST.get('order_key')
#         user_id = request.user.id
#         baskettotal = basket.get_total_price()

#         # Check if order exists
#         if Order.objects.filter(order_key=order_key).exists():
#             pass
#         else:
#             order = Order.objects.create(user_id=user_id, full_name='name', address1='add1',
#                                 address2='add2', total_paid=baskettotal, order_key=order_key)
#             order_id = order.pk

#             for item in basket:
#                 OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

#         return JsonResponse({'success': 'Return something'})
        


# def payment_confirmation(data):
#     Order.objects.filter(order_key=data).update(billing_status=True)


# def user_orders(request):  # sourcery skip: inline-immediately-returned-variable
#     user_id = request.user.id
#     orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
#     return orders


# def basket_summary(request):
#     basket = Basket(request)
#     return render(request, 'basket/summary.html', {'basket': basket})


# def basket_add(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         product_qty = int(request.POST.get('productqty'))
#         # product = get_object_or_404(product, id=product_id)
#         basket.add(product=product, qty=product_qty)

#         basketqty = basket.__len__()
#         return JsonResponse({'qty': basketqty})


# def basket_delete(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         basket.delete(product=product_id)

#         basketqty = basket.__len__()
#         baskettotal = basket.get_total_price()
#         return JsonResponse({'qty': basketqty, 'subtotal': baskettotal})


# def basket_update(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         product_qty = int(request.POST.get('productqty'))
#         basket.update(product=product_id, qty=product_qty)

        # basketqty = basket.__len__()
        # basketsubtotal = basket.get_subtotal_price()
        # return JsonResponse({'qty': basketqty, 'subtotal': basketsubtotal})

    
def checkout_billing_info(request):
    return render(request, 'checkout_billing_info.html')

def checkout(request):
    return render(request, 'checkout.html')

def shopping_cart(request):
    return render (request,'shopping_cart.html')





