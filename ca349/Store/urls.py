from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('products/', views.products, name='products'),
    path('products/<str:catagory>/', views.products, name='products'),
]