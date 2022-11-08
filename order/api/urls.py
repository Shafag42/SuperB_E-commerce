from django.urls import path
from .views import WishlistAPIView
from rest_framework.authtoken import views

urlpatterns = [
    path('wishlist/', WishlistAPIView.as_view({'get': 'list'}), name = "wishlists"),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]