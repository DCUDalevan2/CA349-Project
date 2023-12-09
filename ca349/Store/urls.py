from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('products/', views.products, name='products'),
    path('products/<str:category>/', views.products, name='products'),
    path('item/<int:item_id>/', views.item, name='item'),

]
