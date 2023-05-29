import datetime
from django.views import generic

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from product.serializers import *
from product.models import *


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


# all crud
# class ProductView(viewsets.ModelViewSet):
#     serializer_class = ProductDetailsSerializer
#     queryset = Product.objects.all()

#specific
class ProductView(APIView):
    def get(self, request, product_id=None):
        if product_id is not None:
            try:
                product = Product.objects.get(id=product_id)
                serializer = ProductDetailsSerializer(product)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response({"Product not found"}, status=404)
        else:
            queryset = Product.objects.all()
            serializer = ProductDetailsSerializer(queryset, many=True)
            return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ProductDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductImageView(APIView):
    def post(self, request):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product']
            thumbnail = request.FILES['thumbnail']
            
            # time of upload
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            
            # saving
            file_path = f'media/{product_id}_{timestamp}.jpg' 
            with open(file_path, 'wb') as f:
                for chunk in thumbnail.chunks():
                    f.write(chunk)
            serializer.save(file_path=file_path)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductVariantView(APIView):
    def get(self, request):
        queryset = ProductVariant.objects.all()
        serializer = ProductVariantSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ProductVariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductVariantPriceView(APIView):
    def get(self, request):
        queryset = ProductVariantPrice.objects.all()
        serializer = ProductVariantPriceSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ProductVariantPriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
