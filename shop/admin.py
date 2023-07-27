from django.contrib import admin
from .models import Products,Cart,Order,OrderItem,Address

# Register your models here.

admin.site.register(Cart)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)