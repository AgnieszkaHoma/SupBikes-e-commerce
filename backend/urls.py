from django.contrib import admin
from django.urls import path, include
from . import views
from . views import UserEditProfileView, DeleteProductView


urlpatterns = [
    path('', views.home, name="home"),
    path('register',views.register, name="register"),
    path('loginPage',views.loginPage, name="loginPage"),
    path('signout',views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('all_products', views.ProductList.as_view(), name="all_products"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('profile/<username>/', views.profile, name='profile'),
    path('categories', views.categories, name="categories"),
    path('delivery', views.delivery, name="delivery"),
    path('payment_methods', views.payment_methods, name="payment_methods"),
    path('products/', views.ProductList.as_view()),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('edit_profile', UserEditProfileView.as_view(), name='edit_profile'),
    path('add_product', views.AddProductView.as_view(), name='add_product'),
    path('product/<pk>/delete_product', views.DeleteProductView.as_view(), name='delete_product'),
]
