from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.categoryName}"
    
class Bid(models.Model):
    bid = models.IntegerField(default=0)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="bidder")

    def __str__(self):
        return f"{self.bid}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    imageURL = models.CharField(max_length=1000, blank=True, null=True)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="biddingPrice")
    isActive = models.BooleanField(default=True)
    lister = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, related_name="listingWatchlist")

    def __str__(self):
        return f"{self.title}"
    
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingComment")
    comment = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.author} comment on {self.listing}"

