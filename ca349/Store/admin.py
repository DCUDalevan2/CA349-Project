from django.contrib import admin
from .models import Category, Product, Memory, Colour
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Colour)
admin.site.register(Memory)
