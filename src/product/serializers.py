from rest_framework import serializers
from .models import *


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['title', 'sku', 'description',]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product', 'file_path']

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['variant_title', 'variant', 'product']

class ProductVariantPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = ['product_variant_one', 'product_variant_two', 'product_variant_three', 'price', 'stock', 'product']