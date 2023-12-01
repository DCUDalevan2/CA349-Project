from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.category_name)


class Memory(models.Model):
    memory = models.CharField(max_length=10)

    def __str__(self):
        return str(self.memory)


class Colour(models.Model):
    colour = models.CharField(max_length=10)

    def __str__(self):
        return str(self.colour)


class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    cover_pic = models.ImageField(default='placeholder.png', blank=True)

    def __str__(self):
        return str(self.name)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False
