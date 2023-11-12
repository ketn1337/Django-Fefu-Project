from io import BytesIO
from os import name
from PIL import Image
from django.core.files import File
from pytils.translit import slugify


from django.db import models
from users.models import User
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55)
    ordering = models.IntegerField(default=0)


    class Meta:
        ordering = ['ordering']
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.title
    
    def unique_slug(self):
        unique_slug = slugify(self.title)
        return '{}'.format(unique_slug)
    
    def save(self, *args, **kwargs):
        self.slug = self.unique_slug()
        return super(Category, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("category", kwargs={'category_slug': self.slug})
    
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    vendor = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, default="product")

    slug = models.SlugField(null=True, max_length=55)
    description = models.TextField(blank=True, null=True)
    
    price = models.DecimalField(default=0 ,max_digits=6, decimal_places=2)
    add_date = models.DateTimeField(default=timezone.now)
    change_date = models.DateTimeField(default=timezone.now)
    
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ['-add_date']


    def save(self, *args, **kwargs):
        if not self.id:
            self.add_date = timezone.now()
        self.change_date = timezone.now()
        self.slug = self.unique_slug()
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def unique_slug(self):
        unique_slug = slugify(self.title)
        return '{}'.format(unique_slug)
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'product_slug': self.slug})
    