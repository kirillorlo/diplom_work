from django.urls import path
from . import views
from .views import login, list_products


urlpatterns = [
       path('', views.home, name='home'),
       path('about', views.about, name='about'),
       path('registration/', views.registration, name='registration'),
       path('products/', list_products, name='lists_products'),
       path('login/', login, name='login'),
       path('product/<int:product_id>/', views.product_detail, name='product_detail'),
       path('order/create/', views.create_order, name='create_order'),
       path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]
