from multiprocessing import context
from supbike import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
from .models import *
from .forms import *
import folium
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def home(request):
    return render(request, "backend/index.html")

def register(request):
    
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('register')
        
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = name
        myuser.last_name = surname
        
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to GFG- Django Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('loginPage.html')       
        
    return render(request, "backend/register.html")

def signout(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        
        user = authenticate(username=username, password=password1)
        
        if user is not None:
            login(request, user)
            name = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "backend/index.html",{"name":name})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "backend/loginPage.html")

def activate(request, uidb64, token):
    try: 
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
        
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'backend/message_send.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'backend/contact.html', context)

def about(request):
    m = folium.Map(location=[39.10628257922106, -84.51275072023525], zoom_start=16)
    folium.Marker([39.10628257922106, -84.51275072023525], icon=folium.Icon(color='red', icon='map-marker')).add_to(m)
    m = m._repr_html_()
    context = {
        'm': m, 
    }
    return render(request, 'backend/about.html', context)

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'backend/profile.html', {"user" : user})

def address(request):
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            form.save()
    form = ShippingAddressForm()
    context = {'form': form}
    return render(request, 'backend/profile.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'backend/product_detail.html', {'product': product})

def categories(request):
    return render(request, 'backend/categories.html')

def delivery(request):
    return render(request, 'backend/delivery.html')

class ProductList(ListView):
    model = Product
    template_name = 'backend/prod.html'

def product_detail(request, product_id):
    product = Product.objects.get(pk = product_id)
    return render(request, 'backend/product_detail.html', {'product': product})

class UserEditProfileView(LoginRequiredMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'backend/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user

class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'backend/add_product.html'
    fields = ['name', 'brand', 'category', 'size', 'image', 'price', 'description']
    success_url = reverse_lazy('home')

class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'backend/delete_product.html'
    success_url = reverse_lazy('home')
    
def cart(request):  
    return render(request, 'backend/cart.html')
    
def checkout(request):
    return render(request, 'backend/checkout.html')

def wishlist(request):
    return render(request, 'backend/wishlist.html')

class UpdateProductView(UpdateView):
    model = Product
    form_class = EditProductForm
    template_name = 'backend/update_product.html'
 
    
class Search(ListView):
    model = Product
    template_name = 'backend/search.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(name__icontains=query)
    
def summary(request):  
    return render(request, 'backend/summary.html')

def bikes(request):  
    return render(request, 'backend/bikes.html')

def clothes(request):  
    return render(request, 'backend/clothes.html')

def accesories(request):  
    return render(request, 'backend/accesories.html')

def helmets(request):  
    return render(request, 'backend/helmets.html')

def components(request):  
    return render(request, 'backend/components.html')

def orders(request):  
    return render(request, 'backend/orders.html')

def users(request):  
    return render(request, 'backend/users.html')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')