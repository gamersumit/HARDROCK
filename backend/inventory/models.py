from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100, blank=False, null = False)
    image = models.ImageField(upload_to = "inventory/", blank=True, null = True)  # Store the image URL
    content = models.CharField(max_length=10000, blank=True, null = True)   
    price = models.IntegerField(blank=False, null = False)
    quantity = models.IntegerField(blank=False, null = False)
    category = models.CharField(max_length=100)