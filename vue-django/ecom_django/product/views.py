from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)# converting query set objects into python data type
        # print("this",serializer.data)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)