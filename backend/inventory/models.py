from django.db import models


# Create your models here.

class Inventory(models.Model):

    name = models.CharField(max_length=100, blank=False, null = False)
    img_source = models.CharField(max_length=1000, blank=False, null=False)  # Store the image URL
    content = models.CharField(max_length=10000, blank=True, null = True)
    price = models.IntegerField(blank=False, null = False)
    quantity = models.IntegerField(max_length=20, blank=False, null = False)