from sre_parse import State
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

DELIVERY_CHOICES = (
    ('F', 'FedEx'),
    ('U', 'UPS'),
    ('DH', 'DHL'), 
    ('DP', 'DPD'),
)

PAYMENT_CHOICES = (
    ('C', 'Cash'), 
    ('V', 'Visa'),
    ('P', 'PayU'),
    ('PP', 'PayPal'),
)

STATUS_CHOICES = (
    ('Order placed', 'Order placed'), 
    ('Order confirmed', 'Order confirmed') ,
    ('Order accepted for implementation', 'Order accepted for implementation'),
    ('Order shipped', 'Order shipped'), 
    ('Order canceled', 'Order canceled'),
)  

CATEGORY_CHOICES = (
    ('B', 'Bikes'),
    ('C', 'Clothes'), 
    ('A', 'Accessories'),
    ('Co', 'Components'),
)
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length = 2, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, null=True)
    description =  models.TextField(null=True, blank=True)
    
    def __str__(self):
      return self.name
  
    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug' : self.slug
        })
  
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.city
    
class DiscountCode(models.Model):
    code = models.CharField(max_length=30, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return self.code
    
class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    discountCode = models.ForeignKey(DiscountCode, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True, blank=True)
    delivery = models.CharField(choices = DELIVERY_CHOICES, max_length = 2, default = 'Choose a supplier')
    payment = models.CharField(choices = PAYMENT_CHOICES, max_length = 2, default = 'Choose a payment method')
    orderedProducts = models.CharField(ShopCart, max_length = 200, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    deliveryPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    priceForAll =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(choices= STATUS_CHOICES, max_length=50, default = 'Status')
    # coupon = models.ForeignKey(DiscountCode, on_delete=models.SET_NULL, blank=True, null=True) 
    
    def __str__(self):
        return str(self.createdAt)
    
class Review(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    content = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating
    
class Contact(models.Model):
    email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.email
