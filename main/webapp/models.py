from django.db import models

# Create your models here.


class Announce(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=2024)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    published_at = models.DateField()
