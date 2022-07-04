from django.urls import path

from shopconfigapp import views

app_name = 'shopconfig'

urlpatterns = [
    path('shopconfig/', views.shopconfig, name='shopbase')
]
