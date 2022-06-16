from django.contrib import admin
from .models import Product, ShippingAddress, DiscountCode, Contact, UserOrder, OrderItem, Customer

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'brand', 'category', 'price')
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(DiscountCode)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'email', 'title', 'message')
admin.site.register(Contact, ContactAdmin)
admin.site.register(UserOrder)
admin.site.register(OrderItem)