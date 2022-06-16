from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserChangeForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        
class EditProfileForm(UserChangeForm):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','password')
        
class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'brand', 'category', 'size', 'image', 'price', 'description']    
        
class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price','description')