
from django.urls import path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_main, name='shop_main'),
    path('item/<int:id>', views.shop_item, name='shop_item'),
    path('cart/', views.shop_cart, name='shopcart'),
    path('order/', views.shop_order, name='shoporder'),
    path('orderph/', views.ph_order, name='phorder'),
]