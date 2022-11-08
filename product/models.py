from django.db import models
from django.db.models import Avg, Count
from django.conf import settings

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=50)
    is_navbar=models.BooleanField(default=True)
    parent_category_id=models.ForeignKey("category", on_delete=models.CASCADE, null= True, blank=True, related_name = "category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural= "categories"

class collection(models.Model):
    name=models.CharField(max_length=50)
    category_id=models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name=models.CharField(max_length=50)
    # product_id=models.ForeignKey('product',on_delete=models.CASCADE)

    def __str__(self):
        return self.name 


class product(models.Model):
    name=models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.IntegerField(default=0)
    discounted_price = models.FloatField(null=True)  # type: ignore
    sell_price = models.FloatField(null=True)    # type: ignore
    quick_overview=models.TextField()
    description=models.TextField()
    slug = models.SlugField(max_length=250)
    review_sayi= models.PositiveIntegerField(default=0)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer_id')
    test = models.CharField(max_length=255, null=True, blank=True)
    category_id=models.ForeignKey(category, on_delete=models.CASCADE)
    
    
    @property
    def discounted_price(self):
        return ((self.price)*(self.discount))/100

    @property
    def sell_price(self):
        return (self.price)-(self.discounted_price) 
    
    def __str__(self):
        return self.name



class Color(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class product_version(models.Model):
    cover_image=models.ImageField(upload_to="images/product_version")
    quantity=models.PositiveIntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size, blank= True)
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_id.name}'


class product_images(models.Model):
    img1=models.ImageField(upload_to="images/product_images")
    img2=models.ImageField(upload_to="images/product_images")
    img3=models.ImageField(upload_to="images/product_images")
    product_id=models.ForeignKey(product_version, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id.product_id.name
   

class reviews(models.Model):
    Rates = [
        (1, "20"),
        (2, "40"),
        (3, "60"),
        (4, "80"),
        (5, "100"),
    ]
    price_rating = models.IntegerField(choices=Rates)
    value_rating = models.IntegerField(choices=Rates)
    quality_rating = models.IntegerField(choices=Rates)
    nickname = models.CharField(max_length=100)
    review = models.TextField(verbose_name="Review")
    summary = models.CharField(max_length=100)
    dated = models.DateTimeField(auto_now=True)
    product_id = models.ForeignKey(product_version, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name="reviews"
        verbose_name_plural="reviews"
        
    def __str__(self):
        return self.nickname

