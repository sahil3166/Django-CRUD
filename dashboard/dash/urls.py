from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('category/', category, name='category'),
    path('products/', products, name='products'),
    path('view/', read, name='read'),
    path('delete/', delete, name='delete'),
    path('update/', update, name='update'),
    path('category/add/', categoryAdd, name='categoryAdd'),
    path('category/categoryDelete/<id>', categoryDelete, name='categoryDelete'),
    path('category/categoryUpdate/<id>/', categoryUpdate, name='categoryUpdate'),
    path('products/add/', productAdd, name='productAdd'),
    path('products/productDelete/<id>/', productDelete),
    path('products/productUpdate/<id>/', productUpdate, name='productUpdate'),
    path('products/productView/<id>/', productView),
]
