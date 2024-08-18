from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    aboutme = models.CharField(max_length=255, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    # def __str__(self):
    #     return self.name


# class Customer(models.Model):
#     first_name = models.CharField(max_length=100, null=True, blank=True)
#     last_name = models.CharField(max_length=100, null=True, blank=True)
#     phone = models.IntegerField(null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     password = models.CharField(max_length=50, null=True, blank=True)
#
#     def register(self):
#         self.save()
#
#     @staticmethod
#     def get_customer_by_email(email):
#         try:
#             return Customer.objects.get(email=email)
#         except:
#             return False
#
#     def if_exists(self):
#         if Customer.objects.filter(email=self.email):
#             return True
#
#         return False


class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_name', default=1)
    description = models.CharField(max_length=250, blank=True, null=True)

    # @staticmethod
    # def get_products_by_id(ids):
    #     return Products.objects.filter(id=ids)
    #
    # @staticmethod
    # def get_all_products():
    #     return Products.objects.all()
    #
    # @staticmethod
    # def get_all_products_by_category_id(category_id):
    #     if category_id:
    #         return Products.objects.filter(category=category_id)
    #     else:
    #         return Products.get_all_products()


class ProductImage(models.Model):
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    # def place_order(self):
    #     self.save()
    #
    # @staticmethod
    # def get_orders_by_customer(customer_id):
    #     return Order.objects.filter(customer=customer_id).order_by('-date')


print(Category.get_all_categories())
