from django.contrib import admin
from . models import Product,Collection,Shopping
from django.contrib import admin

# Register your models here.

admin.site.register(Product)
admin.site.register(Collection)

admin.site.register(Shopping)

