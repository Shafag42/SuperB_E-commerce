from django.contrib import admin
from .models import category, collection,product,product_version,product_images,reviews,Manufacturer,Size,Color

admin.site.register (category)
admin.site.register (collection)
admin.site.register (product)
admin.site.register (product_version)
admin.site.register (product_images)
admin.site.register (reviews)
admin.site.register (Manufacturer)
admin.site.register (Size)
admin.site.register (Color)


# Register your models here.
