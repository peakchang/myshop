
from django.urls import path

from shopconfigapp import views

app_name = 'shopconfig'

urlpatterns = [
    path('shopconfig/', views.shopconfig, name='shopbase'),
    path('shop_group/', views.shop_group, name='shopgroup'),
    path('item_list/', views.item_list, name='itemlist'),
    # path('item_form/', views.item_form, name='itemform'),
    # path('item_update/<int:pk>', views.item_update, name='itemupdate'),

    path('in_item_form/', views.in_item_form, name='itemform'),

    path('wark_ajax/', views.work_ajax, name='workajax'),
    path('test/', views.test, name='test'),
]