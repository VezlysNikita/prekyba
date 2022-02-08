from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm


class User(AbstractUser):
    pass

class Listing(models.Model):
    name = models.CharField(max_length=50),
    dateCreated = models.DateTimeField(auto_now_add=True),
    owner = models.ForeignKey(User, on_delete=models.CASCADE),
    startBid = models.FloatField(null=True),
    endBid = models.FloatField(null=True),
    wish = models.ManyToManyField("app.Model"),
    photo = models.CharField(null=True),
    active = models.BooleanField(default=False),
    category = models.CharField(max_length=50)


class Bids(models.Model):
     bid = models.IntegerField(),     
     user = models.ForeignKey(User, on_delete=models.RESTRICT)