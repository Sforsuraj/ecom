from django.contrib import admin
from .models import shop,shop_detail,user_review,billing_address,shipping_address,shop_cart,category

# Register your models here.
admin.site.register(shop)
admin.site.register(shop_detail)
admin.site.register(user_review)
admin.site.register(billing_address)
admin.site.register(shipping_address)
admin.site.register(shop_cart)
admin.site.register(category)