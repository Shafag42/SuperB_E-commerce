from django.db import models
from django_countries.fields import CountryField
from product.models import product, product_version
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
User = get_user_model()
from decimal import Decimal
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    full_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)  # type: ignore




class Basket(models.Model):
    ...
    # """
    # A base Basket class, providing some default behaviors that
    # can be inherited or overrided, as necessary.
    # """

    # def __init__(self, request):
    #     self.session = request.session
    #     basket = self.session.get(settings.BASKET_SESSION_ID)
    #     if settings.BASKET_SESSION_ID not in request.session:
    #         basket = self.session[settings.BASKET_SESSION_ID] = {}
    #     self.basket = basket

    # def add(self, product, qty):
    #     """
    #     Adding and updating the users basket session data
    #     """
    #     product_id = str(product.id)

    #     if product_id in self.basket:
    #         self.basket[product_id]["qty"] = qty
    #     else:
    #         self.basket[product_id] = {"price": str(product.regular_price), "qty": qty}

    #     self.save()

    # def __iter__(self):
    #     """
    #     Collect the product_id in the session data to query the database
    #     and return products
    #     """
    #     product_ids = self.basket.keys()
    #     products = product.objects.filter(id__in=product_ids)  # type: ignore
    #     basket = self.basket.copy()

    #     for product in products:
    #         basket[str(product.id)]["product"] = product

    #     for item in basket.values():
    #         item["price"] = Decimal(item["price"])
    #         item["total_price"] = item["price"] * item["qty"]
    #         yield item

    # def __len__(self):
    #     """
    #     Get the basket data and count the qty of items
    #     """
    #     return sum(item["qty"] for item in self.basket.values())

    # def update(self, product, qty):
    #     """
    #     Update values in session data
    #     """
    #     product_id = str(product)
    #     if product_id in self.basket:
    #         self.basket[product_id]["qty"] = qty
    #     self.save()

    # def get_subtotal_price(self):
    #     return sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

    # def get_total_price(self):

    #     subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

    #     shipping = Decimal(0.00) if subtotal == 0 else Decimal(11.50)
    #     return subtotal + Decimal(shipping)

    # def delete(self, product):
    #     """
    #     Delete item from session data
    #     """
    #     product_id = str(product)

    #     if product_id in self.basket:
    #         del self.basket[product_id]
    #         self.save()

    # def clear(self):
    #     # Remove basket from session
    #     del self.session[settings.BASKET_SESSION_ID]
    #     self.save()

    # def save(self):
    #     self.session.modified = True


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(product_version, on_delete=models.CASCADE,blank=True, null=True)

    class Meta(object):
          verbose_name = 'WishList'
          verbose_name_plural = 'WishLists'
          
    def __str__(self):
          return f"{self.user}"




class CheckoutBilling(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='First Name', help_text='Max 255 character')
    last_name = models.CharField(max_length=50,verbose_name='Last Name', help_text='Max 255 character')
    company = models.TextField(verbose_name='Company')
    email = models.EmailField(verbose_name='Email Address')
    address = models.TextField(verbose_name='Street Address')
    country = CountryField(max_length=255, verbose_name='Country')
    telephone = models.CharField(max_length=25 ,verbose_name='Telephone')
    fax = models.CharField(max_length=50, verbose_name='Fax')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Checkout Billing"
        verbose_name_plural = "Checkout Billings"

    def __str__(self):
        return self.first_name

    

class Checkout(models.Model):
      address=models.CharField(max_length=100)
      created_at=models.DateField(auto_now_add=True)
      updated_at=models.DateField(auto_now=True)


      def __str__(self):
        return self.address

class CheckoutShipping(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='First Name', help_text='Max 255 character')
    last_name = models.CharField(max_length=50,verbose_name='Last Name', help_text='Max 255 character')
    company = models.TextField(verbose_name='Company')
    email = models.EmailField(verbose_name='Email Address')
    address = models.TextField(verbose_name='Street Address')
    country = CountryField(max_length=255, verbose_name='Country')
    telephone = models.CharField(max_length=25 ,verbose_name='Telephone')
    fax = models.CharField(max_length=50, verbose_name='Fax')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Checkout Shipping"
        verbose_name_plural = "Checkout Shipping"

    def __str__(self):
        return self.first_name



class ShoppingCart(models.Model):
    product_name=models.CharField(max_length=200)
    img = models.ImageField(upload_to = "images/")
    unit_price=models.CharField(max_length=10)
    qty=models.CharField(max_length=20)
    subtotal=models.CharField(max_length=25)
    coupon=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=20)
    state=models.TextField()
    country=models.TextField(blank=False)

    class Meta:
        verbose_name = "Shopping Cart"
        verbose_name_plural = "Shopping Cart"
  
    def __str__(self):
        return self.product_name



