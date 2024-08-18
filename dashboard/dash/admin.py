from django.contrib import admin
from .models import User, Category, Products, Order

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Order)
