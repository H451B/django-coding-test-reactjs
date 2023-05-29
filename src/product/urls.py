from django.urls import path,include
from django.views.generic import TemplateView

from product.views.product import *
from product.views.variant import VariantView, VariantCreateView, VariantEditView


from django.urls import path,include
from rest_framework import routers

# router=routers.DefaultRouter()
# router.register(r'',ProductView,'product')
# router.register(r'productvariant',ProductVariantView,'product-variant')


app_name = "product"



urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    
    path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),

    # product
    # path('all/', include(router.urls)),
    path('all/', ProductView.as_view(), name='product-details'),
    path('all/<int:product_id>/', ProductView.as_view(), name='product-details'),

    #image
    path('image/', ProductImageView.as_view(), name='product-image'),

    #product variants
    path('product-variants/', ProductVariantView.as_view(), name='product-variant'),

    #productvariant prices
    path('product-variant-prices/', ProductVariantPriceView.as_view(), name='product-variant-price-create'),

    

]
