from django.db import models
from account.models import CustomUser
from inventory.models import Inventory

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    # Add any other fields you may need

    