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
    ('H', 'Helmets'),
    ('Co', 'Components'),
)
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length = 2, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description =  models.TextField(null=True, blank=True)
    
    def __str__(self):
      return self.name
  
    def get_absolute_url(self):
        return reverse('product_detail', args=(str(self.id)))
       
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name     

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.address
    
class DiscountCode(models.Model):
    code = models.CharField(max_length=30, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return self.code
    
class Contact(models.Model):
    email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.email

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    date_ordered = models.DateTimeField(null=True)

class UserOrder(models.Model):
    ref_code = models.CharField(max_length=15, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_ordered = models.BooleanField(default=False, null=True)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
 
    def get_cart_items(self):
        return self.items.all()
    
    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code) 