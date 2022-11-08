from django.urls import path
from .views import Product_list, Productview

urlpatterns = [
    # path('product-list/', Product_ListView.as_view(), name='product-list'),
    # path('product-detail/',Product_ListView.as_view(), name='product_detail'),
    # path('product-list/', product_list, name='product-list'),
    path('product-detail/<int:pk>/',Productview.as_view(), name='product_detail'),
    path('product-list/',Product_list.as_view(), name='product-list')
    
]