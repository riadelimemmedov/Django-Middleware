from django.db import models

# Create your models here.

#!Customer
class Customer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=5,decimal_places=2)#max_digits => max number of number,decimal_places => max number after comma
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)