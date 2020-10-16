from django.contrib import admin

# Register your models here.
from shop_order.models import Order, Orderdetail

admin.site.register(Order)
admin.site.register(Orderdetail)
