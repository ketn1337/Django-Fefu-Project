from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("ordering",)
    
    def __str__(self):
        return self.title
    

class Product(models.Model):

   class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)

    image = models.ImageField(upload_to="media/uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="media/uploads/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self):
        return self.title