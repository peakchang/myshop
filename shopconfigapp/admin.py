from django.contrib import admin

# Register your models here.
from shopconfigapp.models import ShopCategory, ShopItem

admin.site.register(ShopCategory)
admin.site.register(ShopItem)
