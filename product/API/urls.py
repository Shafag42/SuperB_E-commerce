from django.urls import path
from .views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ProductAPIView, ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RegisterView

urlpatterns = [
    path('product/',  ProductAPIView.as_view()),
    path('product/<int:pk>/', ProductAPIView.as_view()),
    path("",ListAPIView.as_view(),name="category_list"),  # type: ignore
    path("create/", CreateAPIView.as_view(),name="category_create"),  # type: ignore
    path("update/<int:pk>/",UpdateAPIView.as_view(),name="category_update"),  # type: ignore
    path("delete/<int:pk>/",DestroyAPIView.as_view(),name="category_delete"),  # type: ignore
    path('register',RegisterView.as_view(), name='register'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
