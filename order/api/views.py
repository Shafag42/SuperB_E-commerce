from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from order.models import WishList
from .serializers import WishlistSerializer
from product.models  import product_version
from rest_framework import serializers
from rest_framework import viewsets

class WishlistAPIView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions
    """
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# class WishlistAPIView(APIView):
#     queryset = WishList.objects.all()
#     serializer_class = WishlistSerializer
#     permission_classes = []

#     def get(self, request, *args, **kwargs):
#         first_wishlist, created = WishList.objects.get_or_create(user=request.user)
#         # print(request)
#         # first_wishlist = WishList.objects.all()
#         serializer = self.serializer_class(first_wishlist)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, *args, **kwargs):
#         product_id = request.data.get('product_id')
#         product = product_version.objects.filter(pk=product_id).first()
#         wishlist, created = WishList.objects.get_or_create(user=request.user)

#         if product and product not in wishlist.product.all():  # type: ignore
#             wishlist.product.add(product)  # type: ignore
#         else:
#             wishlist.product.remove(product)  # type: ignore
#         message = {'success': True,
#                    'message': 'Product added to your wishlist.'}
#         return Response(message, status=status.HTTP_201_CREATED)

    