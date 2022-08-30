from time import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import *


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
    condition = models.CharField(max_length=64, default="")
    location = models.CharField(max_length=64, default="")
    dateCreated = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Listing #{self.id}: {self.title} ({self.user.username.title()})"


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)



class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="wishlist")

    class Meta:
        unique_together = (("user", "listing"))



class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    dateCreated = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=2000, blank=True)
    