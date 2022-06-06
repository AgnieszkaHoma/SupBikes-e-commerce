from django.contrib import admin
from .models import Product, ShippingAddress, ShopCart, Order, DiscountCode, Review, Contact

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'brand', 'category', 'price')
admin.site.register(Product, ProductAdmin)

admin.site.register(ShippingAddress)
admin.site.register(ShopCart)
admin.site.register(Order)
admin.site.register(DiscountCode)
admin.site.register(Review)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'email', 'title', 'message')
admin.site.register(Contact, ContactAdmin)
