from rest_framework.response import Response
from rest_framework import status,views
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework import generics
from product.models import product,product_version, category
from rest_framework.views import APIView
from .serializers import ProductSerializer,CategorySerializer,RegisterSerializer
from rest_framework.response import Response
from django.http.response import Http404
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

        
class ProductAPIView(APIView):

    # READ a single Product
    def get_object(self, pk):  # sourcery skip: raise-from-previous-error
        try:
            return product.objects.get(pk=pk)
        except product.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):  # sourcery skip: assign-if-exp
        if pk:
            data = self.get_object(pk)
        else:
            data = product.objects.all()

        serializer = ProductSerializer(data, many=True)

        return Response(serializer.data)

   
    def post(self, request, *args, **kwargs):
        form_data = request.data
        serializer = ProductSerializer(data=form_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=201)

    def put(self, request, pk=None, format=None):
        product_to_update = product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=product_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Product Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        product_to_delete =  product.objects.get(pk=pk)

        product_to_delete.delete()

        return Response({
            'message': 'Product Deleted Successfully'
        })


class ListTodoAPIView(ListAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class CreateTodoAPIView(CreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class UpdateTodoAPIView(UpdateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class DeleteTodoAPIView(DestroyAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

# class SubscriberEmailView(generics.ListCreateAPIView):
#     serializer_class = SubscriberEmailSerializer
#     queryset = SubscriberEmail.objects.all()
