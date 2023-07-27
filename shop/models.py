from django.db import models

from authentication.models import User




class Products(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100,null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Approved', 'Approved'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Approved')




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)