from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

ANNOUNCE_STATUS = (
    ("new", "новая"),
    ("published", 'опубликовано'),
    ("reject", "отклонено"),
)


class Announce(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="announces")
    photo = models.ImageField()
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=2024)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    published_at = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=48, choices=ANNOUNCE_STATUS, default="new")

