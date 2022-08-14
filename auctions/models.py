from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __self__(self):
        return f"{self.username}"
    
    
    


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing")
    title = models.CharField(max_length=64)
    image = models.URLField()
    description = models.CharField(max_length=2000)
    category = models.CharField(max_length=64)
    bid = models.DecimalField(max_digits=10000000, decimal_places=2)

    def __str__(self):
        return f"Listing #{self.id}: {self.title} ({self.user.username.title()})"
